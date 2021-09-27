import datetime
import uuid
from typing import Optional
from pydantic import BaseModel, validator
from src.models.CursoModel import EstadoCursoEnum
from fastapi import HTTPException


class CursoBase(BaseModel):
    id_creador: uuid.UUID
    titulo: str
    descripcion: str

    @validator('titulo')
    def tiene_titulo(cls, titulo: str):
        if not titulo:
            raise HTTPException(status_code=400, detail='Debe proporcionar un título.')
        return titulo

    @validator('descripcion')
    def tiene_descripcion(cls, descripcion: str):
        if not descripcion:
            raise HTTPException(status_code=400, detail='Debe proporcionar una descripción.')
        return descripcion


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
