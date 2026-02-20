from app.data.repository.IUsuarioRepository import IUsuarioRepository
from app.service.IUsuarioService import IUsuarioService
from app.domain.model.usuario import Usuario
from app.seguridad.seguridad import *
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.security import OAuth2PasswordBearer
from fastapi import FastAPI, Depends, HTTPException
from fastapi import status

class UsuarioService(IUsuarioService):
    def __init__(self, usuarioRepository: IUsuarioRepository):
        self.usuarioRepository = usuarioRepository

    def registar_usuario(self, email: str, password: str):
        usuario_existe = self.usuarioRepository.obtener_usuario_email(email)

        if usuario_existe:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="El correo electrónico ya está registrado"
            )
        
        password_hash = encriptar_password(password)

        nuevo_usuario = Usuario(email = email,password_hash = password_hash)

        self.usuarioRepository.insertar_usuario(nuevo_usuario)



    def login (self, email: str, password: str) -> dict:
        usuario_existe = self.usuarioRepository.obtener_usuario_email(email)

        if not usuario_existe or not verificar_password(password, usuario_existe.password_hash):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Email o contraseña incorrectos",
                headers={"WWW-Authenticate": "Bearer"},
            )
        
        
        access_token = crear_token_acceso(data={"sub": usuario_existe.email})

        return {"access_token": access_token, "token_type": "bearer"}
        
        

        