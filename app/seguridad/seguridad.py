from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import JWTError, jwt
import os


#CONFIGURACIÓN
SECRET_KEY = os.getenv("PASSWORD_SERVER")
ALGORITHM = "HS256" 
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def encriptar_password(password: str) -> str:
    return pwd_context.hash(password)

def  verificar_password(password: str, password_encriptada: str) -> bool:
    return pwd_context.verify(password, password_encriptada)

def crear_token_acceso(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt