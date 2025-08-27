# 🚀 Gestor de Tareas con Django

## 📋 Descripción del Proyecto
Este es un proyecto web desarrollado con el framework **Django** que implementa un sistema CRUD (Crear, Leer, Actualizar, Borrar) para la gestión de tareas. La aplicación permite a los usuarios crear una cuenta, iniciar sesión y administrar sus propias tareas. Utiliza **SQLite** como base de datos, lo que la hace fácil de configurar y ejecutar localmente.

## ✨ Funcionalidades
- **Autenticación de usuarios:** Permite a los usuarios registrarse y acceder a su cuenta.
- **Creación de tareas:** Cada usuario puede crear nuevas tareas con su respectiva información.
- **Visualización de tareas:** Los usuarios pueden ver una lista de todas sus tareas.
- **Edición de tareas:** Permite modificar las tareas existentes.
- **Eliminación de tareas:** Los usuarios pueden borrar tareas que ya no necesitan.
- **Marcado de importancia:** Permite a los usuarios marcar tareas como importantes para priorizarlas.

## ⚙️ Tecnologías
- Python 3.x
- Django 3.x 
- SQLite3
- HTML

## ▶️ Cómo ejecutar el proyecto
1.  Clona este repositorio en tu máquina local.
2.  Navega al directorio del proyecto en tu terminal.
3.  Crea un entorno virtual y actívalo (recomendado):
    ```bash
    python -m venv venv
    # En Windows:
    venv\Scripts\activate
    # En macOS/Linux:
    source venv/bin/activate
    ```
4.  Instala las dependencias del proyecto:
    ```bash
    pip install django
    ```
5.  Aplica las migraciones de la base de datos para crear las tablas necesarias:
    ```bash
    python manage.py migrate
    ```
6.  (Opcional) Crea un superusuario para acceder al panel de administración de Django:
    ```bash
    python manage.py createsuperuser
    ```
7.  Inicia el servidor de desarrollo:
    ```bash
    python manage.py runserver
    ```
8.  Abre tu navegador web y visita `http://127.0.0.1:8000` para ver la aplicación.
