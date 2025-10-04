# app/dependencies.py

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError
from sqlalchemy.orm import Session

from . import crud, models, schemas, security
from .database import SessionLocal
from .redis_client import get_redis_client

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/token")


def get_db():
    """
    Dependency to provide a SQLAlchemy database session.
    Opens a session at the start of the request and closes it at the end,
    even if exceptions occur.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


async def get_current_active_user(
    token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)
):
    """
    Dependency to retrieve the current active user from a JWT token.
    Decodes the token, extracts the email, and fetches the user from the database.
    """
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = security.decode_access_token(token)
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
        token_data = schemas.TokenData(email=email)
    except JWTError:
        raise credentials_exception

    user = crud.get_user_by_email(db, email=token_data.email)
    if user is None:
        raise credentials_exception

    return user


def get_redis():
    """
    Dependency to provide a Redis client.
    Useful if you want to use Redis directly in your routers.
    """
    return get_redis_client()
