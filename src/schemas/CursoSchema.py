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


class EditarCurso(BaseModel):
    nuevo_titulo: str
    nueva_descripcion: str


# En esta clase se le agregan todos los atributos particulares para la creación
class CreateCursoRequest(CursoBase):
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


# Esto es lo que se va a devolver cuando se este "leyendo" un Curso
class CursoResponse(CursoBase):
    id: uuid.UUID
    estado: EstadoCursoEnum
    fecha_creacion: datetime.datetime
    fecha_actualizacion: Optional[datetime.datetime]

    class Config:
        orm_mode = True

class EditCursoRequest(EditarCurso):
    @validator('nuevo_titulo')
    def tiene_titulo(cls, nuevo_titulo: str):
        if not nuevo_titulo:
            raise HTTPException(status_code=400, detail='Debe proporcionar un título.')
        return nuevo_titulo

    @validator('nueva_descripcion')
    def tiene_descripcion(cls, nueva_descripcion: str):
        if not nueva_descripcion:
            raise HTTPException(status_code=400, detail='Debe proporcionar una descripción.')
        return nueva_descripcion