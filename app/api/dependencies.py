from fastapi import Depends
from sqlalchemy.orm import Session
from app.data.database.config import obtener_sesion
from app.data.repository.UsuarioRepository import UsuarioRepository
from app.service.UsuarioService import UsuarioService
from app.service.IUsuarioService import IUsuarioService

def get_usuario_service(db: Session = Depends(obtener_sesion)) -> IUsuarioService:
    repo = UsuarioRepository(db)

    return UsuarioService(repo)