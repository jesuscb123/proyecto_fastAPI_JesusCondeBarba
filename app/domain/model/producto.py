from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List
from app.data.database.config import Base 

class Producto(Base):
    __tablename__ = "productos"
    
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column()
    
    usuario_id: Mapped[int] = mapped_column(ForeignKey("usuarios.id"))
    dueño: Mapped["Usuario"] = relationship(back_populates="productos")

    ingredientes: Mapped[List["Ingrediente"]] = relationship(back_populates="producto")