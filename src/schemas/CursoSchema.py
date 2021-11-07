import datetime
import uuid
from typing import Optional
from pydantic import BaseModel, validator
from src.models.CursoModel import EstadoCursoEnum, Curso
from fastapi import HTTPException
from src.models.CursoModel import TipoCursoEnum, SuscripcionCursoEnum


class CursoBase(BaseModel):
    id_creador: str
    titulo: str
    descripcion: str
    hashtags: str
    tipo: str
    examenes: str
    suscripcion: str
    ubicacion: str


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

    @validator('tipo')
    def tiene_tipo(cls, tipo: str):
        if not tipo:
            raise HTTPException(status_code=400, detail='Debe proporcionar un tipo.')
        try:
            TipoCursoEnum(tipo)
        except ValueError as e:
            raise HTTPException(status_code=400, detail='Debe proporcionar un tipo válido: (' + str(e) + ')')
        return tipo

    @validator('suscripcion')
    def tiene_suscripcion(cls, suscripcion: str):
        if not suscripcion:
            raise HTTPException(status_code=400, detail='Debe proporcionar una suscripcion.')
        try:
            SuscripcionCursoEnum(suscripcion)
        except ValueError as e:
            raise HTTPException(status_code=400, detail='Debe proporcionar una suscripción válida: (' + str(e) + ')')
        return suscripcion


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