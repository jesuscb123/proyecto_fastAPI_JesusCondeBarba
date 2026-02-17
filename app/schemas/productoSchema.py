from pydantic import BaseModel
from typing import List
from schemas.ingredienteSchema import ingredienteSchema

class ProductoSchema(BaseModel):
    nombre: str
    ingredientes: List[ingredienteSchema]