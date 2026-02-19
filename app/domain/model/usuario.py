from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.data.database.config import Base 
from typing import List

class Usuario(Base):
    __tablename__ = "usuarios"

    id: Mapped[int] = mapped_column(primary_key=True)

    email: Mapped[str] = mapped_column()
    password_hash: Mapped[str] = mapped_column()

    productos: Mapped[List["Producto"]] = relationship(back_populates="dueño")