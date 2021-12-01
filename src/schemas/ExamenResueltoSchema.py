import datetime
import uuid
from typing import Optional, List
from pydantic import BaseModel

from src.schemas import RespuestaSchema


class ExamenResueltoBase(BaseModel):
    id_cursada: uuid.UUID
    id_examen: uuid.UUID


class CreateExamenResueltoRequest(ExamenResueltoBase):
    respuestas: List[RespuestaSchema.CreateRespuestaRequest]


class ExamenResueltoResponse(ExamenResueltoBase):
    id: uuid.UUID
    fecha_creacion: datetime.datetime
    fecha_actualizacion: Optional[datetime.datetime]
    respuestas: List[RespuestaSchema.RespuestaResponse]
    estado: str
    corrector: Optional[str]
    nota: Optional[int]

    class Config:
        orm_mode = True
