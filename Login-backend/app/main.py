from fastapi import FastAPI

from . import models
from .database import engine
from .routers import auth, users

# Esta línea le dice a SQLAlchemy que cree todas las tablas definidas en nuestros
# modelos (heredando de la clase Base) si no existen ya en la base de datos.
# NOTA: Para producción, es más robusto manejar esto con migraciones (Alembic).
models.Base.metadata.create_all(bind=engine)

# Instancia principal de la aplicación FastAPI
app = FastAPI(
    title="Auth API Base",
    description="Un proyecto base para autenticación de usuarios con FastAPI y Flutter.",
    version="0.1.0",
    # Opcional: Configuración para la documentación
    swagger_ui_parameters={"syntaxHighlight.theme": "obsidian"},
)

# Incluimos los routers en la aplicación principal.
# Todas las rutas definidas en auth.router y users.router ahora son parte de la app.
app.include_router(auth.router)
app.include_router(users.router)


@app.get("/", tags=["Root"])
def read_root():
    """
    Endpoint raíz para verificar que la API está funcionando.
    """
    return {"message": "Welcome to the Python-José Auth API!"}
