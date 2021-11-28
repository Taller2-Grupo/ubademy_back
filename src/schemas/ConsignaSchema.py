import datetime
import uuid
from typing import Optional, List
from pydantic import BaseModel


class ConsignaBase(BaseModel):
    enunciado: str


# Esto es lo que se va a devolver cuando se este "leyendo" un Colaborador
class ConsignaResponse(ConsignaBase):
    id: uuid.UUID
    fecha_creacion: datetime.datetime
    fecha_actualizacion: Optional[datetime.datetime]
    id_examen: uuid.UUID

    class Config:
        orm_mode = True
