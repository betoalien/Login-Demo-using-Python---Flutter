# app/crud.py

import json
from sqlalchemy.orm import Session

from . import models, schemas, security
from .redis_client import get_redis_client

# TTL for cached user data (in seconds)
USER_CACHE_TTL = 600  # 10 minutes

# Redis keys pattern
USER_EMAIL_KEY = "user:email:{email}"  # maps email -> user JSON


def get_user_by_email(db: Session, email: str):
    """
    Get a user by email. Uses Redis cache-aside strategy.
    1. Try Redis first (email key).
    2. On miss, query Postgres, then cache result.
    """
    r = get_redis_client()
    key = USER_EMAIL_KEY.format(email=email.lower())

    # --- Try cache ---
    cached_user = r.get(key)
    if cached_user:
        try:
            data = json.loads(cached_user)
            # Reconstruct a lightweight User object (not bound to the session)
            user = models.User(
                id=data["id"],
                email=data["email"],
                hashed_password=data["hashed_password"],
                created_at=data["created_at"],
            )
            return user
        except (json.JSONDecodeError, KeyError):
            # If cached data is corrupted, delete it and continue with DB
            r.delete(key)

    # --- Fallback to DB ---
    user = db.query(models.User).filter(models.User.email == email).first()
    if user:
        # Serialize and cache
        to_cache = {
            "id": user.id,
            "email": user.email,
            "hashed_password": user.hashed_password,
            "created_at": user.created_at.isoformat() if user.created_at else None,
        }
        r.setex(key, USER_CACHE_TTL, json.dumps(to_cache))

    return user


def create_user(db: Session, user: schemas.UserCreate):
    """
    Create a new user and invalidate any cache for this email.
    """
    hashed_password = security.get_password_hash(user.password)
    db_user = models.User(email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    # Invalidate cache for this email (if any)
    r = get_redis_client()
    key = USER_EMAIL_KEY.format(email=user.email.lower())
    r.delete(key)

    return db_user


def authenticate_user(db: Session, email: str, password: str):
    """
    Authenticate a user by email and password.
    Uses the same get_user_by_email which is cached.
    """
    user = get_user_by_email(db, email=email)
    if not user:
        return None
    if not security.verify_password(password, user.hashed_password):
        return None
    return user
