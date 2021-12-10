import datetime
import uuid
from typing import Optional
from pydantic import BaseModel, validator
from fastapi import HTTPException


class ColaboradorBase(BaseModel):
    id_curso: uuid.UUID
    username: str



# En esta clase se le agregan todos los atributos particulares para la creación
class CreateColaboradorRequest(ColaboradorBase):
    @validator('username')
    def tiene_username(cls, username: str):
        if not username:
            raise HTTPException(status_code=400, detail='Debe proporcionar un nombre de usuario.')
        return username


class DeleteColaboradorRequest(ColaboradorBase):
    pass


# Esto es lo que se va a devolver cuando se este "leyendo" un Colaborador
class ColaboradorResponse(ColaboradorBase):
    id: uuid.UUID
    fecha_creacion: datetime.datetime
    fecha_actualizacion: Optional[datetime.datetime]

    class Config:
        orm_mode = True
