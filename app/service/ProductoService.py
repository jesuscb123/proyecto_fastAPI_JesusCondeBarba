from app.service.IProductoService import IProductoService
from app.data.repository.IProductoRepository import IProductoRepository
from app.domain.model.producto import Producto
from app.domain.model.ingrediente import Ingrediente
from app.domain.schemas.ingredienteSchema import IngredienteSchema
from app.data.repository.IUsuarioRepository import IUsuarioRepository

class ProductoService(IProductoService):
    def __init__(self, productoRepository: IProductoRepository, usuarioRepository: IUsuarioRepository):
        self.productoRepository = productoRepository
        self.usuarioRepository = usuarioRepository
    

    def listar_todos_productos(self) -> list[Producto]:
        return self.productoRepository.listar_todos_productos()


    def listar_productos_usuario(self, usuario_id: int) -> list[Producto]:
        return self.productoRepository.listar_productos_usuario(usuario_id)
    
    def insertar_producto(self, nombre: str, ingredientes: list[IngredienteSchema], dueño_email: str):
        usuario_producto = self.usuarioRepository.obtener_usuario_email(dueño_email)
        obj_ingredientes = [Ingrediente(nombre=ingrediente.nombre) for ingrediente in ingredientes]
        nuevo_producto = Producto(
            nombre = nombre,
            usuario_id = usuario_producto.id,
            ingredientes = obj_ingredientes
        )

        return self.productoRepository.insertar_producto(nuevo_producto)



