# 📋 Gestión de Recetas y Productos (FastAPI + Vue 3)

Este proyecto es una aplicación web completa para la gestión de recetas. Permite a los usuarios registrarse, iniciar sesión y administrar sus propios productos, asociando ingredientes a cada uno. El sistema está construido con una arquitectura moderna, separando el backend (API REST) del frontend (SPA), y está totalmente dockerizado para facilitar su despliegue.
## DEMO

## 🚀 Características Principales

*   **Autenticación Segura**: Registro y Login de usuarios mediante JWT (JSON Web Tokens).
*   **Gestión de Productos**: CRUD completo (Crear, Leer, Actualizar, Borrar) de productos.
*   **Ingredientes**: Asociación de ingredientes a cada producto.
*   **Relaciones**: Cada producto pertenece a un usuario específico ("dueño").
*   **Documentación Interactiva**: Swagger UI y Redoc integrados automáticamente.
*   **Base de Datos**: Persistencia de datos robusta con PostgreSQL.
*   **Frontend Reactivo**: Interfaz de usuario moderna construida con Vue 3 y Vite.

## 🛠️ Tecnologías Utilizadas

### Backend
*   **Lenguaje**: Python 3.10+
*   **Framework API**: [FastAPI](https://fastapi.tiangolo.com/) (Alto rendimiento, validación automática)
*   **ORM**: [SQLAlchemy](https://www.sqlalchemy.org/) (Gestión de base de datos)
*   **Validación**: Pydantic
*   **Autenticación**: Python-Jose (JWT), Passlib (Hashing de contraseñas)

### Frontend
*   **Framework JS**: [Vue.js 3](https://vuejs.org/)
*   **Build Tool**: Vite
*   **Estado**: Pinia
*   **Routing**: Vue Router
*   **Cliente HTTP**: Axios

### Infraestructura
*   **Contenedores**: Docker & Docker Compose
*   **Base de Datos**: PostgreSQL 15
*   **Servidor Web Frontend**: Nginx (en producción/docker)

## 📂 Estructura del Proyecto

```
.
├── app/                # Código fuente del Backend (FastAPI)
│   ├── database/       # Configuración de base de datos
│   ├── model/          # Modelos SQLAlchemy (Tablas)
│   ├── schemas/        # Esquemas Pydantic (Validación)
│   ├── seguridad/      # Lógica de JWT y Hashing
│   └── main.py         # Punto de entrada de la API
├── frontend/           # Código fuente del Frontend (Vue 3)
│   ├── src/            # Componentes, Vistas, Stores
│   ├── public/         # Archivos estáticos
│   └── dockerfile      # Configuración de construcción del frontend
├── docker-compose.yaml # Orquestación de servicios
├── requirements.txt    # Dependencias de Python
└── .env.example        # Plantilla de variables de entorno
```

## 🔧 Instalación y Ejecución

### Requisitos Previos
*   [Docker Desktop](https://www.docker.com/products/docker-desktop/) instalado y en ejecución.
*   Git (opcional, para clonar).

### Pasos para levantar el proyecto

1.  **Clonar el repositorio** (o descargar el código):
    ```bash
    git clone <URL_DEL_REPOSITORIO>
    cd fastApi_JesusCondeBarba
    ```

2.  **Configurar Variables de Entorno**:
    Copia el archivo `.env.example` y renómbralo a `.env`.
    ```bash
    cp .env.example .env
    # En Windows: copy .env.example .env
    ```
    Edita `.env` con tus credenciales preferidas si es necesario (USER, PASSWORD, DB).

3.  **Ejecutar con Docker Compose**:
    Este comando construirá las imágenes del backend y frontend, y levantará la base de datos.
    ```bash
    docker compose up --build
    ```

4.  **Acceder a la Aplicación**:
    *   **Frontend (Vue)**: Abre [http://localhost:8080](http://localhost:8080) en tu navegador.
    *   **Documentación API (Swagger)**: Visita [http://localhost:8000/docs](http://localhost:8000/docs).
    *   **Documentación Alternativa (Redoc)**: Visita [http://localhost:8000/redoc](http://localhost:8000/redoc).

## 🧪 Endpoints Principales

| Método | Endpoint | Descripción | Requiere Auth |
| :--- | :--- | :--- | :---: |
| `POST` | `/login` | Iniciar sesión y obtener token JWT | ❌ |
| `POST` | `/usuarios` | Registrar un nuevo usuario | ❌ |
| `GET` | `/productos` | Listar productos del usuario actual | ✅ |
| `POST` | `/productos` | Crear un nuevo producto con ingredientes | ✅ |
| `GET` | `/productos/todos` | Listar todos los productos (público) | ❌ |

## 👤 Autor
Proyecto realizado como práctica para Libnamic.
- [Repositorio GitHub](https://github.com/jesuscb123/proyecto_fastAPI_JesusCondeBarba)

----
[Versión con JSONB (Rama separada)](https://github.com/jesuscb123/proyecto_fastAPI_JesusCondeBarba/tree/pruebas-jsonb)
