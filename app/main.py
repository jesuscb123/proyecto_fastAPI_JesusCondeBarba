from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import select
from app.database.database import SessionLocal, engine, Base
from app.model.producto import Producto
from app.model.ingrediente import Ingrediente
from app.schemas.productoSchema import ProductoSchema
from app.schemas.usuarioSchema import UsuarioSchema
from app.schemas.usuarioCreado import UsuarioCreado
from app.model.usuario import Usuario
from app.seguridad.seguridad import *
from fastapi.security import OAuth2PasswordRequestForm
from jose import jwt, JWTError
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import joinedload
from fastapi.middleware.cors import CORSMiddleware
from typing import List

Base.metadata.create_all(bind = engine)
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def obtener_sesion():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def obtener_usuario_actual(token: str = Depends(oauth2_scheme), db: Session = Depends(obtener_sesion)):
    credentials_exception = HTTPException(status_code=401, detail="No se pudo validar el token")
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    usuario = db.query(Usuario).filter(Usuario.email == email).first()
    if usuario is None:
        raise credentials_exception
    return usuario


@app.get("/productos")
def listar_productos_usuario(db: Session = Depends(obtener_sesion), usuario_actual: Usuario = Depends(obtener_usuario_actual)):
    query = (
        select(Producto)
        .options(joinedload(Producto.dueño)) 
        .where(Producto.usuario_id == usuario_actual.id)
    )
    productos_respuesta = []
    productos =  db.execute(query).scalars().all()

    for producto in productos:
        producto_schema = ProductoSchema(
            id = producto.id, nombre = producto.nombre, 
            dueño_email=producto.dueño.email,
            ingredientes = producto.ingredientes
        )
        productos_respuesta.append(producto_schema)

    return productos_respuesta

@app.get("/productos/todos", response_model=List[ProductoSchema])
def listar_todos_productos(db: Session = Depends(obtener_sesion)):
    query = select(Producto).options(joinedload(Producto.dueño))
    productos = db.execute(query).scalars().unique().all()

    productos_respuesta = []

    for producto in productos:
        producto_schema = ProductoSchema(
        id = producto.id, nombre = producto.nombre, 
        dueño_email=producto.dueño.email,
        ingredientes = producto.ingredientes
    )
        productos_respuesta.append(producto_schema)
    
    return productos_respuesta
        
           

@app.post("/productos", response_model=ProductoSchema)
def insertar_producto(
    producto: ProductoSchema, 
    db: Session = Depends(obtener_sesion),
    usuario_actual: Usuario = Depends(obtener_usuario_actual)
    ) -> Producto:
    nuevo_producto = Producto(nombre = producto.nombre, usuario_id = usuario_actual.id)

    for ingrediente in producto.ingredientes:
        objeto_ingrediente = Ingrediente(nombre = ingrediente.nombre)
        nuevo_producto.ingredientes.append(objeto_ingrediente)

    db.add(nuevo_producto)
    db.commit()
    db.refresh(nuevo_producto)

    return nuevo_producto



@app.post("/usuarios", response_model=UsuarioSchema)
def registrar_usuario(usuario_creado: UsuarioCreado, db: Session = Depends(obtener_sesion)) -> Usuario:
    usuario_existe = db.query(Usuario).filter(Usuario.email == usuario_creado.email).first()
    if usuario_existe:
        raise HTTPException(status_code=400, detail="El email ya está registrado")
    
    password_encriptada = encriptar_password(usuario_creado.password)

    nuevo_usuario = Usuario(
        email=usuario_creado.email,
        password_hash=password_encriptada 
    )

    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)

    return nuevo_usuario


@app.post("/login")
def login(
    form_data: OAuth2PasswordRequestForm = Depends(), 
    db: Session = Depends(obtener_sesion)
):
    usuario = db.query(Usuario).filter(Usuario.email == form_data.username).first()

    if not usuario or not verificar_password(form_data.password, usuario.password_hash):
        raise HTTPException(
            status_code=401, 
            detail="Email o contraseña incorrectos",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token = crear_token_acceso(data={"sub": usuario.email})

    return {"access_token": access_token, "token_type": "bearer"}












    
