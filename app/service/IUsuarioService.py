from abc import ABC, abstractmethod
from app.domain.model.usuario import Usuario

class IUsuarioService(ABC):
    @abstractmethod
    def registar_usuario(self, email: str, password: str):
        pass

    @abstractmethod
    def login (self, email: str, password: str) -> dict:
        pass