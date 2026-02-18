from pydantic import BaseModel
from typing import List
from app.schemas.ingredienteSchema import IngredienteSchema

class ProductoSchema(BaseModel):
    nombre: str
    ingredientes: List[IngredienteSchema]

    dueño_email: str | None = None

    model_config = {
        "from_attributes": True
    }