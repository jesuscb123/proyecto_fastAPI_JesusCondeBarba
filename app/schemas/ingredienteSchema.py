from pydantic import BaseModel

class IngredienteSchema(BaseModel):
    nombre: str