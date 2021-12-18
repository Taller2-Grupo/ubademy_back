import datetime
import uuid
from typing import Optional, List
from pydantic import BaseModel

from src.schemas import RespuestaSchema, CursadaSchema


class ExamenResueltoBase(BaseModel):
    id_examen: uuid.UUID


class CreateExamenResueltoRequest(ExamenResueltoBase):
    id_curso: uuid.UUID
    username: str
    respuestas: List[RespuestaSchema.CreateRespuestaRequest]


class CorreccionRespuestaRequest(BaseModel):
    id_respuesta: uuid.UUID
    es_correcta: bool


class CorregirExamenRequest(BaseModel):
    id_examen_resuelto: uuid.UUID
    corrector: str
    correcciones: List[CorreccionRespuestaRequest]


class ExamenResueltoResponse(ExamenResueltoBase):
    id: uuid.UUID
    fecha_creacion: datetime.datetime
    fecha_actualizacion: Optional[datetime.datetime]
    respuestas: List[RespuestaSchema.RespuestaResponse]
    estado: str
    corrector: Optional[str]
    nota: Optional[int]
    cursada: CursadaSchema.CursadaResponse

    class Config:
        orm_mode = True
