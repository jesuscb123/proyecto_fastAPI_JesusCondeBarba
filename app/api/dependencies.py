from fastapi import Depends
from sqlalchemy.orm import Session
from app.data.database.config import obtener_sesion
from app.data.repository.UsuarioRepository import UsuarioRepository
from app.service.UsuarioService import UsuarioService
from app.service.IUsuarioService import IUsuarioService
from app.service.IProductoService import IProductoService
from app.service.ProductoService import ProductoService
from app.data.repository.ProductoRepository import ProductoRepository
from fastapi import Depends, HTTPException, status
from jose import JWTError, jwt
from app.seguridad.seguridad import SECRET_KEY, ALGORITHM 
from app.data.repository.ProductoRepository import ProductoRepository
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/usuarios/login")

def obtener_usuario_actual(
    token: str = Depends(oauth2_scheme), 
    db: Session = Depends(obtener_sesion)
):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED, 
        detail="No se pudo validar el token"
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    
    repo = UsuarioRepository(db)
    usuario = repo.obtener_usuario_email(email)
    
    if usuario is None:
        raise credentials_exception
    return usuario


def get_usuario_service(db: Session = Depends(obtener_sesion)) -> IUsuarioService:
    usuarioRepository = UsuarioRepository(db)

    return UsuarioService(usuarioRepository)

def get_producto_service(db: Session = Depends(obtener_sesion)) -> IProductoService:
    productoRepository = ProductoRepository(db)
    usuarioRepository = UsuarioRepository(db)
    
    return ProductoService(productoRepository, usuarioRepository)