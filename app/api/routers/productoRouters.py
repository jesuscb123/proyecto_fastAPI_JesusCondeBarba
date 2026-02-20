from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List
from app.domain.schemas.productoSchema import ProductoSchema
from app.service.IProductoService import IProductoService
from app.api.dependencies import get_producto_service, obtener_usuario_actual
from app.domain.model.usuario import Usuario

router = APIRouter(prefix="/productos", tags=["Productos"])


@router.post("/", response_model=ProductoSchema, status_code=status.HTTP_201_CREATED)
def crear_producto(
    producto_creado: ProductoSchema, 
    productoService: IProductoService = Depends(get_producto_service),
    usuario_actual: Usuario = Depends(obtener_usuario_actual)
):

    producto = productoService.insertar_producto(
        nombre = producto_creado.nombre, 
        ingredientes = producto_creado.ingredientes, 
        dueño_email= usuario_actual.email)
  

    return ProductoSchema(
        nombre = producto.nombre,
        ingredientes = producto.ingredientes,
        dueño_email= usuario_actual.email
    )


@router.get("/", response_model=List[ProductoSchema])
def listar_todos_productos(productoService: IProductoService = Depends(get_producto_service)):
    productos = productoService.listar_todos_productos()
    
    return [
        ProductoSchema(
            nombre=p.nombre,
            dueño_email=p.dueño.email if p.dueño else "Sin dueño",
            ingredientes=[{"nombre": ing.nombre} for ing in p.ingredientes]
        ) for p in productos
    ]


@router.get("/mis-productos", response_model=List[ProductoSchema])
def listar_productos_usuario(
    productoService: IProductoService = Depends(get_producto_service),
    usuario_actual: Usuario = Depends(obtener_usuario_actual) 
):
    productos = productoService.listar_productos_usuario(usuario_actual.id)
    
    return [
        ProductoSchema(
            nombre=p.nombre,
            dueño_email=usuario_actual.email, 
            ingredientes=[{"nombre": ing.nombre} for ing in p.ingredientes]
        ) for p in productos
    ]