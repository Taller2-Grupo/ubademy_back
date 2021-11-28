import datetime
import uuid
from typing import Optional, List
from pydantic import BaseModel

from src.schemas import ConsignaSchema


class ExamenBase(BaseModel):
    id_curso: uuid.UUID
    nombre: str


# En esta clase se le agregan todos los atributos particulares para la creación
class CreateExamenRequest(ExamenBase):
    consignas: List[str]


# Esto es lo que se va a devolver cuando se este "leyendo" un Colaborador
class ExamenResponse(ExamenBase):
    id: uuid.UUID
    fecha_creacion: datetime.datetime
    fecha_actualizacion: Optional[datetime.datetime]
    consignas: List[ConsignaSchema.ConsignaResponse]

    class Config:
        orm_mode = True
