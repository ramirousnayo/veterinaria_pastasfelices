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
   git clone https://github.com/ramirousnayo/veterinaria_pastasfelices.git
   cd veterinaria_pastasfelices
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

```text
.
├── config/                 # Configuración del proyecto Django
│   ├── settings/           # Ajustes divididos por entorno
│   │   ├── base.py
│   │   ├── local.py
│   │   └── production.py
│   ├── asgi.py
│   ├── urls.py
│   └── wsgi.py
├── fichas/                 # Aplicación principal de registros veterinarios
│   ├── fixtures/           # Datos iniciales para la base de datos
│   │   └── datos_iniciales.json
│   ├── migrations/         # Migraciones de base de datos
│   ├── admin.py            # Configuración del panel de administración
│   ├── apps.py
│   ├── models.py           # Modelos: Dueño, Mascota, ConsultaMedica
│   ├── urls.py             # URLs específicas de la app fichas
│   └── views.py            # Lógica de las vistas (CBV y funciones)
├── templates/              # Plantillas HTML
│   └── fichas/             # Vistas de la aplicación
│       ├── base.html       # Estructura base compartida
│       ├── inicio.html     # Dashboard principal
│       ├── dueno_*.html    # Plantillas para la gestión de dueños
│       ├── mascota_*.html  # Plantillas para la gestión de mascotas
│       └── consulta_*.html # Plantillas para la gestión de consultas
├── manage.py               # Script de gestión de Django
├── requirements.txt        # Dependencias del proyecto
├── .env.example            # Ejemplo de configuración para variables de entorno
└── .gitignore              # Archivos ignorados por Git
```

## Vistas Disponibles 🖥️

- `/`: Inicio con estadísticas.
- `/duenos/`: Listado y gestión de dueños.
- `/mascotas/`: Listado y gestión de mascotas.
- `/consultas/`: Listado y historial de consultas médicas.

---
Proyecto desarrollado con ❤️ para la gestión veterinaria.
