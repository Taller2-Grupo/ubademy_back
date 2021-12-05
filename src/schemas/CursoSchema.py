import datetime
import uuid
from typing import Optional, List
from pydantic import BaseModel, validator
from src.models.CursoModel import EstadoCursoEnum
from fastapi import HTTPException
from src.models.CursoModel import TipoCursoEnum, SuscripcionCursoEnum
from src.schemas import ColaboradorSchema


class CursoBase(BaseModel):
    id_creador: Optional[str]
    titulo: Optional[str]
    descripcion: Optional[str]
    hashtags: Optional[str]
    tipo: Optional[str]
    suscripcion: Optional[str]
    ubicacion: Optional[str]


class EditarCurso(BaseModel):
    nuevo_titulo: Optional[str]
    nueva_descripcion: Optional[str]
    nuevo_estado: Optional[str]
    nuevos_hashtags: Optional[str]
    nuevo_tipo: Optional[str]
    nueva_suscripcion: Optional[str]
    nueva_ubicacion: Optional[str]


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
    colaboradores: Optional[List[ColaboradorSchema.ColaboradorResponse]]

    class Config:
        orm_mode = True
