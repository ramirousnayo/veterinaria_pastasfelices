# Veterinaria Patas Felices 🐾

Sistema de gestión para clínicas veterinarias que permite llevar un registro detallado de dueños, mascotas y consultas médicas.

## Características 🚀

- **Gestión de Dueños**: Registro completo de propietarios (Nombre, RUT, Teléfono, Email, Dirección).
- **Gestión de Mascotas**: Registro de pacientes (Nombre, Especie, Raza, Fecha de Nacimiento) vinculados a sus dueños.
- **Consultas Médicas**: Historial de atenciones médicas con detalle de motivo, diagnóstico, tratamiento y costo.
- **Panel de Control**: Resumen rápido con el total de registros en el sistema.

## Requisitos Técnicos 🛠️

- **Framework**: Django 6.0.3
- **Lenguaje**: Python 3.x
- **Base de Datos**: PostgreSQL (Producción) / SQLite (Desarrollo)
- **Variables de Entorno**: Gestionadas con `python-dotenv`

## Instalación ⚙️

1. **Clonar el repositorio**:
   ```bash
   git clone <url-del-repositorio>
   cd veterinaria_patasfelices
   ```

2. **Crear y activar un entorno virtual**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```

3. **Instalar dependencias**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configurar el archivo `.env`**:
   Copia el archivo `.env.example` a `.env` y ajusta tus credenciales:
   ```bash
   cp .env.example .env
   ```

5. **Realizar las migraciones**:
   ```bash
   python manage.py migrate
   ```

6. **Crear un superusuario (opcional)**:
   ```bash
   python manage.py createsuperuser
   ```

7. **Ejecutar el servidor**:
   ```bash
   python manage.py runserver
   ```

## Estructura del Proyecto 📁

- `config/`: Archivos de configuración del proyecto Django.
- `fichas/`: Aplicación principal que contiene la lógica de negocio (modelos, vistas, urls).
- `templates/`: Plantillas HTML para la interfaz de usuario.
- `db.sqlite3`: Base de datos local (solo desarrollo).

## Vistas Disponibles 🖥️

- `/`: Inicio con estadísticas.
- `/duenos/`: Listado y gestión de dueños.
- `/mascotas/`: Listado y gestión de mascotas.
- `/consultas/`: Listado y historial de consultas médicas.

---
Proyecto desarrollado con ❤️ para la gestión veterinaria.
