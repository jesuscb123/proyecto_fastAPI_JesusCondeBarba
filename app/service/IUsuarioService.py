from abc import ABC, abstractmethod
from app.domain.model.usuario import Usuario

class IUsuarioService(ABC):
    @abstractmethod
    def obtener_usuario_email(self, email: str) -> Usuario:
        pass

    def insertar_usuario(self, usuario: Usuario):
        pass