from app.service.IProductoService import IProductoService
from app.data.repository.IProductoRepository import IProductoRepository
from app.domain.schemas.productoSchema import ProductoSchema


class ProductoService(IProductoService):
    def __init__(self, productoRepository: IProductoRepository):
        self.productoRepository = productoRepository
    

    def listar_todos_productos(self) -> list[ProductoSchema]:
        productos = self.productoRepository.listar_todos_productos()
        productos_respuesta = []

        for producto in productos:
            producto_schema = ProductoSchema(
            id = producto.id, nombre = producto.nombre, 
            dueño_email=producto.dueño.email,
            ingredientes = producto.ingredientes
            )
            productos_respuesta.append(producto_schema)
        
        return productos_respuesta
    

    