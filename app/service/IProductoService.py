from abc import ABC, abstractmethod
from app.domain.model.producto import Producto
from app.domain.schemas.ingredienteSchema import IngredienteSchema

class IProductoService(ABC):
    @abstractmethod
    def listar_todos_productos(self) -> list[Producto]:
        pass

    @abstractmethod
    def listar_productos_usuario(elf, usuario_id: int) -> list[Producto]:
        pass

    @abstractmethod
    def insertar_producto(self, nombre: str, ingredientes: list[IngredienteSchema], dueño_email: str):
        pass