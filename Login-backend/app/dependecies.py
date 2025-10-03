from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError
from sqlalchemy.orm import Session

from . import crud, models, schemas, security
from .database import SessionLocal

# Esta instancia de OAuth2PasswordBearer es una "dependencia" que busca un token JWT
# en el encabezado de autorización de la petición.
# 'tokenUrl' apunta al endpoint de login para que la documentación interactiva sepa a dónde ir.
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/token")


def get_db():
    """
    Dependencia para obtener una sesión de la base de datos.

    Abre una sesión al inicio de la petición y se asegura de cerrarla al final,
    incluso si ocurren errores.
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
    Dependencia para obtener el usuario actual a partir de un token JWT.

    Valida el token, decodifica su contenido (payload) y busca al usuario
    correspondiente en la base de datos.
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
        
    # En una app real, podrías verificar si el usuario está activo aquí
    # if not user.is_active:
    #     raise HTTPException(status_code=400, detail="Inactive user")
        
    return user
