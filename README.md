# FASTAPI DE RECETAS (DOCKER)
Este proyecto es una API REST que permite crear y consultar recetas/productos añadiendo los ingredientes necesarios.
## TECNOLOGÍAS UTILIZADAS
- PostgreSQL
- SQLAlchemy (ORM)
- Docker & Docker Compose
- Pydantic (Validación de datos)

## CÓMO EJECUTAR EL PROYECTO
1. Tener instalado Docker Desktop.
2. Levantar el entorno
    - Clona el repositorio y ejecuta el siguiente comando en la raíz del proyecto:
      
          docker compose up --build
3. Documentación de la API
    - Una vez que el contenedor esté corriendo, puedes acceder a la documentación interactiva (Swagger UI) para probar las rutas: [enlace para acceder a Swagger UI](http://localhost:8000/docs)
