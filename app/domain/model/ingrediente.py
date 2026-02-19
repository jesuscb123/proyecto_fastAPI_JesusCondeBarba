from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from app.data.database.config import Base

class Ingrediente(Base):
    __tablename__ = "ingredientes"

    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column()
    
    producto_id: Mapped[int] = mapped_column(ForeignKey("productos.id"))

    producto: Mapped["Producto"] = relationship(back_populates="ingredientes")