import os
from datetime import datetime, timedelta, timezone
from jose import JWTError, jwt
from passlib.context import CryptContext
from dotenv import load_dotenv

# Cargamos las variables de entorno desde el archivo .env
load_dotenv()

# --- Configuración de Seguridad ---
# Clave secreta para firmar los tokens JWT. ¡Debe ser secreta!
SECRET_KEY = os.getenv("SECRET_KEY")
# Algoritmo de encriptación
ALGORITHM = os.getenv("ALGORITHM", "HS256")
# Tiempo de expiración del token en minutos
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 30))

# --- Hashing de Contraseñas ---

# Creamos un contexto para passlib, especificando el algoritmo a usar (bcrypt)
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    Verifica que una contraseña en texto plano coincida con un hash guardado.
    """
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str) -> str:
    """
    Genera el hash de una contraseña en texto plano.
    """
    return pwd_context.hash(password)

# --- Gestión de Tokens JWT ---

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    """
    Crea un nuevo token de acceso JWT.
    """
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        # Si no se provee un tiempo, el token expira en 15 minutos por defecto
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def decode_access_token(token: str):
    """
    Decodifica un token para obtener su payload.
    Esta función será usada por nuestras dependencias.
    Lanza una excepción JWTError si el token es inválido.
    """
    # La excepción JWTError será capturada por la dependencia que llame a esta función
    payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    return payload
