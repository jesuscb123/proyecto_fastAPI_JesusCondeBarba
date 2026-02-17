from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import select
from app.database.database import SessionLocal, engine, Base
from app.model.producto import Producto
from app.schemas.productoSchema import ProductoSchema

Base.metadata.create_all(bind = engine)
app = FastAPI()


def obtener_sesion():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



@app.get("/productos")
def listar_productos(db: Session = Depends(obtener_sesion)):
    query = select(Producto)
    return db.execute(query).scalars().all()

@app.post("/productos", response_model=ProductoSchema)
def insertar_producto(producto: ProductoSchema, db: Session = Depends(obtener_sesion)):
    lista_ingredientes = []
    for ingrediente in producto.ingredientes:
        lista_ingredientes.append(ingrediente.model_dump()) #convertir a diccionario cada ingrediente para poder guardarlo en formato json
    nuevo_producto = Producto(nombre = producto.nombre, ingredientes = lista_ingredientes)

    db.add(nuevo_producto)
    db.commit()
    db.refresh(nuevo_producto)

    return nuevo_producto








    
