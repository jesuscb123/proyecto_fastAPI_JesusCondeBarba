from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import List
from app.database.database import Base 
from sqlalchemy.dialects.postgresql import JSONB

class Producto(Base):
    __tablename__ = "productos"
    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column()
    ingredientes: Mapped[List] = mapped_column(JSONB, default=[])