import datetime
import uuid
from typing import Optional, List
from pydantic import BaseModel

from src.schemas import ConsignaSchema


class ExamenBase(BaseModel):
    nombre: str


class CreateExamenRequest(ExamenBase):
    id_curso: uuid.UUID
    consignas: List[str]


class EditExamenRequest(ExamenBase):
    id: uuid.UUID
    consignas: List[str]


class ExamenResponse(ExamenBase):
    id: uuid.UUID
    id_curso: uuid.UUID
    fecha_creacion: datetime.datetime
    fecha_actualizacion: Optional[datetime.datetime]
    consignas: List[ConsignaSchema.ConsignaResponse]
    estado: str

    class Config:
        orm_mode = True
