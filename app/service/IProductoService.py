from abc import ABC, abstractmethod
from app.domain.model.producto import Producto

class IProductoService(ABC):
    @abstractmethod
    def listar_todos_productos(self) -> list[Producto]:
        pass

    @abstractmethod
    def listar_productos_usuario(self, email: str) -> list[Producto]:
        pass