from datetime import datetime
from pydantic import BaseModel, EmailStr

# --- Token Schemas ---

class Token(BaseModel):
    """
    Schema para la respuesta del token de acceso.
    """
    access_token: str
    token_type: str


class TokenData(BaseModel):
    """
    Schema para los datos contenidos dentro de un token JWT.
    """
    email: EmailStr | None = None


# --- User Schemas ---

class UserBase(BaseModel):
    """
    Schema base para los datos de un usuario.
    Contiene los campos comunes.
    """
    email: EmailStr


class UserCreate(UserBase):
    """
    Schema para la creación de un nuevo usuario.
    Hereda de UserBase y añade la contraseña.
    """
    password: str


class UserPublic(UserBase):
    """
    Schema para los datos de un usuario que se pueden exponer públicamente.
    Hereda de UserBase y añade los campos que no son sensibles.
    
    Importante: NUNCA incluye el campo 'hashed_password'.
    """
    id: int
    created_at: datetime

    class Config:
        """
        Configuración para que Pydantic funcione con modelos de ORM (SQLAlchemy).
        Permite que el schema se cree a partir de un objeto de la base de datos.
        """
        from_attributes = True
