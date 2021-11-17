import datetime
import uuid
from typing import Optional
from pydantic import BaseModel


class ColaboradorBase(BaseModel):
    id_curso: Optional[uuid.UUID]
    username: Optional[str]


# En esta clase se le agregan todos los atributos particulares para la creación
class CreateColaboradorRequest(ColaboradorBase):
    pass


# Esto es lo que se va a devolver cuando se este "leyendo" un Colaborador
class ColaboradorResponse(ColaboradorBase):
    id: uuid.UUID
    fecha_creacion: datetime.datetime
    fecha_actualizacion: Optional[datetime.datetime]

    class Config:
        orm_mode = True
