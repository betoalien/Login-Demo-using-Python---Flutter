from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from .. import crud, models, schemas
from ..dependecies import get_db, get_current_active_user

router = APIRouter(
    prefix="/api/users",
    tags=["Users"]
)

@router.post("/", response_model=schemas.UserPublic, status_code=status.HTTP_201_CREATED)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    """
    Endpoint para registrar un nuevo usuario en la base de datos.
    """
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )
    return crud.create_user(db=db, user=user)


@router.get("/me", response_model=schemas.UserPublic)
def read_users_me(current_user: models.User = Depends(get_current_active_user)):
    """
    Endpoint para obtener el perfil del usuario actualmente autenticado.

    Requiere un token JWT válido en el encabezado de autorización.
    La dependencia 'get_current_active_user' se encarga de la validación.
    """
    return current_user
