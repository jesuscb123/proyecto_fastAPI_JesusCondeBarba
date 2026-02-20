from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import select
from app.data.database.config import SessionLocal, engine, Base
from app.domain.model.producto import Producto
from app.domain.model.ingrediente import Ingrediente
from app.domain.schemas.productoSchema import ProductoSchema
from app.domain.schemas.usuarioSchema import UsuarioSchema
from app.domain.schemas.usuarioCreado import UsuarioCreado
from app.domain.model.usuario import Usuario
from app.seguridad.seguridad import *
from fastapi.security import OAuth2PasswordRequestForm
from jose import jwt, JWTError
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import joinedload
from fastapi.middleware.cors import CORSMiddleware
from typing import List
from app.api.routers import usuariosRouters
from app.api.routers import productoRouters

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

app.include_router(usuariosRouters.router)
app.include_router(productoRouters.router)



















    
