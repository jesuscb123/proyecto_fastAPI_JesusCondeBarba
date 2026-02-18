from pydantic import BaseModel

class IngredienteSchema(BaseModel):
    nombre: str

    model_config = {
        "from_attributes": True
    }