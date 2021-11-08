import datetime
import uuid
from typing import Optional

from pydantic import BaseModel, validator
from fastapi import HTTPException

from src.models.CursadaModel import EstadoCursadaEnum


class CursadaBase(BaseModel):
    username: Optional[str]

class InscribirAlumno(CursadaBase):

    @validator('username')
    def tiene_username(cls, username: str):
        if not username:
            raise HTTPException(status_code=400, detail='Debe proporcionar un nombre de usuario.')
        return username


class CursadaResponse(CursadaBase):
    id: uuid.UUID
    estado: EstadoCursadaEnum
    fecha_creacion: datetime.datetime
    fecha_actualizacion: Optional[datetime.datetime]

    class Config:
        orm_mode = True