from app.data.repository.IUsuarioRepository import IUsuarioRepository
from sqlalchemy.orm import Session
from app.domain.model.usuario import Usuario

class UsuarioRepository(IUsuarioRepository):
    def __init__(self, db: Session):
        self.db = db

    def obtener_usuario_email(self, email) -> Usuario:
        return self.db.query(Usuario).filter(Usuario.email == email).first()
    
    def insertar_usuario(self, usuario: Usuario):
        self.db.add(usuario)
        self.db.commit()
        self.db.refresh(usuario)
        return usuario