from pydantic import BaseModel, EmailStr

class UsuarioSchema(BaseModel):
    email: str
    
    model_config = {
        "from_attributes": True
    }