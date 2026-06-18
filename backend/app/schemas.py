from pydantic import BaseModel

class TicketCreate(BaseModel):
    titulo: str
    descripcion: str
    estado: str