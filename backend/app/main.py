from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from .database import get_db
from .models import Ticket
from .schemas import TicketCreate

app = FastAPI(
    title="SAP Ticket Manager API",
    version="1.0.0"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Ruta principal
@app.get("/")
def home():
    return {
        "mensaje": "Bienvenido a SAP Ticket Manager API"
    }


# Listar tickets
@app.get("/tickets")
def listar_tickets(db: Session = Depends(get_db)):
    tickets = db.query(Ticket).all()
    return tickets


# Crear ticket
@app.post("/tickets")
def crear_ticket(ticket: TicketCreate, db: Session = Depends(get_db)):
    nuevo_ticket = Ticket(
        titulo=ticket.titulo,
        descripcion=ticket.descripcion,
        estado=ticket.estado
    )

    db.add(nuevo_ticket)
    db.commit()
    db.refresh(nuevo_ticket)

    return {
        "mensaje": "Ticket creado correctamente",
        "id": nuevo_ticket.id
    }


# Actualizar ticket
@app.put("/tickets/{ticket_id}")
def actualizar_ticket(
    ticket_id: int,
    ticket: TicketCreate,
    db: Session = Depends(get_db)
):
    ticket_db = db.query(Ticket).filter(
        Ticket.id == ticket_id
    ).first()

    if not ticket_db:
        raise HTTPException(
            status_code=404,
            detail="Ticket no encontrado"
        )

    ticket_db.titulo = ticket.titulo
    ticket_db.descripcion = ticket.descripcion
    ticket_db.estado = ticket.estado

    db.commit()

    return {
        "mensaje": "Ticket actualizado correctamente"
    }


# Eliminar ticket
@app.delete("/tickets/{ticket_id}")
def eliminar_ticket(
    ticket_id: int,
    db: Session = Depends(get_db)
):
    ticket_db = db.query(Ticket).filter(
        Ticket.id == ticket_id
    ).first()

    if not ticket_db:
        raise HTTPException(
            status_code=404,
            detail="Ticket no encontrado"
        )

    db.delete(ticket_db)
    db.commit()

    return {
        "mensaje": "Ticket eliminado correctamente"
    }