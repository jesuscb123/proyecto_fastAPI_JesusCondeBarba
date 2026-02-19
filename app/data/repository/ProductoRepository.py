from app.domain.model.producto import Producto
from app.data.repository.IProductoRepository import IProductoRepository
from sqlalchemy.orm import Session
from sqlalchemy import select
from sqlalchemy.orm import joinedload

class ProductoRepository(IProductoRepository):
    def __init__(self, db: Session):
        self.db = db

    def listar_todos_productos(self):
        query = select(Producto).options(joinedload(Producto.dueño))
        return self.db.execute(query).scalars().unique().all()
    
    def listar_productos_usuario(self, usuario_id: int):
       query = (
        select(Producto)
        .options(joinedload(Producto.dueño)) 
        .where(Producto.usuario_id == usuario_id)
    )
       
       return self.db.execute(query).scalars().all()
    
