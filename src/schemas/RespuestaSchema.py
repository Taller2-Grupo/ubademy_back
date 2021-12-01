import datetime
import uuid
from typing import Optional
from pydantic import BaseModel


class RespuestaBase(BaseModel):
    consigna: str
    resolucion: str


class CreateRespuestaRequest(RespuestaBase):
    pass


class RespuestaResponse(RespuestaBase):
    id: uuid.UUID
    fecha_creacion: datetime.datetime
    fecha_actualizacion: Optional[datetime.datetime]
    id_examen_resuelto: uuid.UUID

    class Config:
        orm_mode = True
