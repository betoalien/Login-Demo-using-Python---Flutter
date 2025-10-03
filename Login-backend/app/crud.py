from sqlalchemy.orm import Session

from . import models, schemas, security


def get_user_by_email(db: Session, email: str):
    """
    Busca y devuelve un usuario por su dirección de correo electrónico.

    Args:
        db: La sesión de la base de datos.
        email: El email del usuario a buscar.

    Returns:
        El objeto User si se encuentra, de lo contrario None.
    """
    return db.query(models.User).filter(models.User.email == email).first()


def create_user(db: Session, user: schemas.UserCreate):
    """
    Crea un nuevo usuario en la base de datos.

    Hashea la contraseña antes de guardarla.

    Args:
        db: La sesión de la base de datos.
        user: Un schema UserCreate con los datos del nuevo usuario.

    Returns:
        El objeto User recién creado.
    """
    hashed_password = security.get_password_hash(user.password)
    db_user = models.User(email=user.email, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def authenticate_user(db: Session, email: str, password: str):
    """
    Autentica a un usuario.

    Compara la contraseña proporcionada en texto plano con la versión
    hasheada almacenada en la base de datos.

    Args:
        db: La sesión de la base de datos.
        email: El email del usuario.
        password: La contraseña en texto plano.

    Returns:
        El objeto User si la autenticación es exitosa, de lo contrario None.
    """
    user = get_user_by_email(db, email=email)
    if not user:
        return None
    if not security.verify_password(password, user.hashed_password):
        return None
    return user
