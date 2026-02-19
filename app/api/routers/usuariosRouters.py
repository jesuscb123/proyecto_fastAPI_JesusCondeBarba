from fastapi import APIRouter, Depends, status
from app.domain.schemas.usuarioSchema import UsuarioSchema
from app.domain.schemas.usuarioCreado import UsuarioCreado
from app.api.dependencies import get_usuario_service
from app.service.IUsuarioService import IUsuarioService
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])

@router.post("/", response_model= UsuarioSchema)
def registrar_usuario(
    usuario_creado: UsuarioCreado,
    usuario_service: IUsuarioService = Depends(get_usuario_service)
):
    return usuario_service.registar_usuario(usuario_creado.email, usuario_creado.password)


@router.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    service: IUsuarioService = Depends(get_usuario_service)
):
    return service.login(form_data.username, form_data.password)