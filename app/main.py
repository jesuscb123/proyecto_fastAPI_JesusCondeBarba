from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import select
from app.database.database import SessionLocal, engine, Base
from app.model.producto import Producto
from app.model.ingrediente import Ingrediente
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
    nuevo_producto = Producto(nombre = producto.nombre)

    for ingrediente in producto.ingredientes:
        objeto_ingrediente = Ingrediente(nombre = ingrediente.nombre)
        nuevo_producto.ingredientes.append(objeto_ingrediente)

    db.add(nuevo_producto)
    db.commit()
    db.refresh(nuevo_producto)

    return nuevo_producto








    
