import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from app.main import app
from app.database import Base
from app.dependecies import get_db

# --- Configuración de la Base de Datos de Prueba ---

# Usaremos una base de datos SQLite en memoria para las pruebas.
# Es rápida y se destruye después de cada ejecución.
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False}, # Requerido para SQLite
    poolclass=StaticPool, # Usar una única conexión para toda la prueba
)

# Creamos una "fábrica" de sesiones de prueba
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# --- Fixtures de Pytest ---

@pytest.fixture(scope="function")
def db_session():
    """
    Fixture para crear una base de datos y una sesión de prueba para cada función de prueba.
    """
    # Crea todas las tablas en la base de datos en memoria
    Base.metadata.create_all(bind=engine)
    
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
        # Destruye todas las tablas después de que la prueba termine
        Base.metadata.drop_all(bind=engine)

@pytest.fixture(scope="function")
def client(db_session):
    """
    Fixture para obtener un cliente de prueba de FastAPI que usa la base de datos de prueba.
    """
    
    def override_get_db():
        """
        Una función de dependencia temporal que reemplaza get_db
        y devuelve nuestra sesión de base de datos de prueba.
        """
        try:
            yield db_session
        finally:
            db_session.close()

    # Reemplazamos la dependencia get_db con nuestra versión de prueba
    app.dependency_overrides[get_db] = override_get_db
    
    # Creamos y devolvemos el cliente de prueba
    yield TestClient(app)
    
    # Limpiamos el override después de la prueba
    app.dependency_overrides.clear()
