import datetime
import uuid
from typing import Optional
from pydantic import BaseModel, validator
from fastapi import HTTPException


class ColaboradorBase(BaseModel):
    id_curso: uuid.UUID
    username: str


class DeleteColaboradorRequest(ColaboradorBase):
    pass


# Esto es lo que se va a devolver cuando se este "leyendo" un Colaborador
class ColaboradorResponse(ColaboradorBase):
    id: uuid.UUID
    fecha_creacion: datetime.datetime
    fecha_actualizacion: Optional[datetime.datetime]

    class Config:
        orm_mode = True
