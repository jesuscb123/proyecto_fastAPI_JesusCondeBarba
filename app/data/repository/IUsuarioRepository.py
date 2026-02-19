from abc import ABC, abstractmethod
from app.domain.model.usuario import Usuario
from app.domain.schemas.usuarioCreado import UsuarioCreado

class IUsuarioRepository(ABC):
    @abstractmethod
    def obtener_usuario_email(self, email: str) -> Usuario:
        pass

    @abstractmethod
    def insertar_usuario(self, usuario: Usuario) -> bool:
        pass


    