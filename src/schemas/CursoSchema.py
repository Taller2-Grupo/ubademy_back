import datetime
import uuid
from typing import Optional
from pydantic import BaseModel, validator
from src.models.CursoModel import EstadoCursoEnum


class CursoBase(BaseModel):
    id_creador: uuid.UUID
    titulo: str
    descripcion: str


    # @validator('cantidad_alumnos')
    # def cantidad_menor_a_50(cls, cantidad):
    #     if cantidad > 50:
    #         raise HTTPException(status_code=400, detail='Bad Request')
    #     return cantidad


# En esta clase se le agregan todos los atributos particulares para la creación, en este caso ninguno.
class CreateCursoRequest(CursoBase):
    pass


# Esto es lo que se va a devolver cuando se este "leyendo" un Curso, en este caso "id" que no se pasa al crear
class CursoResponse(CursoBase):
    id: uuid.UUID
    estado: EstadoCursoEnum
    fecha_creacion: datetime.datetime
    fecha_actualizacion: Optional[datetime.datetime]

    class Config:
        orm_mode = True
