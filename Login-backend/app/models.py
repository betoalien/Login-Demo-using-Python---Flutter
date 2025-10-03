from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func

from .database import Base

class User(Base):
    """
    Modelo de SQLAlchemy para la tabla 'users'.
    
    Esta clase define la estructura de la tabla 'users' en la base de datos.
    SQLAlchemy la utiliza para mapear filas de la tabla a objetos de Python.
    """
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    
    # Establece la fecha de creación por defecto a nivel de base de datos
    created_at = Column(DateTime, server_default=func.now())
