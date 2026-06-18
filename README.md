# SAP Ticket Manager

Sistema de gestión de tickets desarrollado con FastAPI, SQL Server, HTML, CSS y JavaScript.

## Descripción

SAP Ticket Manager es una aplicación web que permite registrar, consultar, actualizar y eliminar tickets de soporte relacionados con incidencias en SAP.

El sistema implementa operaciones CRUD completas mediante una API REST construida con FastAPI y una interfaz web desarrollada con HTML, CSS y JavaScript.

## Tecnologías Utilizadas

### Backend
- Python
- FastAPI
- SQLAlchemy
- SQL Server
- PyODBC

### Frontend
- HTML5
- CSS3
- JavaScript

## Funcionalidades

- Crear tickets
- Listar tickets
- Actualizar tickets
- Eliminar tickets
- Buscar tickets
- Gestión de estados:
  - Abierto
  - En proceso
  - Cerrado

## Estructura del Proyecto

```text
SAP-Ticket-Manager/
│
├── backend/
│   ├── app/
│   │   ├── database.py
│   │   ├── main.py
│   │   ├── models.py
│   │   └── schemas.py
│   │
│   └── requirements.txt
│
└── frontend/
    ├── index.html
    ├── css/
    │   └── style.css
    └── js/
        └── app.js
