from pydantic import BaseModel, EmailStr

class UsuarioCreado(BaseModel):
    email: str
    password: str

