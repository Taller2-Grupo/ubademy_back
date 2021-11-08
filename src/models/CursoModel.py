import datetime
import enum
from typing import Optional

from sqlalchemy import Column, Enum, String
from sqlalchemy.dialects import postgresql
from src.models.Entity import Entity
from src.db.database import Base
from fastapi import HTTPException


class EstadoCursoEnum(str, enum.Enum):
    activo = 'activo'
    bloqueado = 'bloqueado'
    eliminado = 'eliminado'

class TipoCursoEnum(str, enum.Enum):
    idioma = 'idioma'
    programacion = 'programacion'
    multimedia = 'multimedia'

class SuscripcionCursoEnum(str, enum.Enum):
    gratuito = 'gratuito'
    pago = 'pago'

class Curso(Base, Entity):
    __tablename__ = "cursos"
    id_creador = Column(String, nullable=False)
    titulo = Column(String, nullable=False)
    descripcion = Column(String, nullable=False)
    estado = Column(Enum(EstadoCursoEnum), nullable=False)
    hashtags = Column(String, nullable=True)
    tipo = Column(Enum(TipoCursoEnum), nullable=False)
    examenes = Column(String, nullable=True)
    suscripcion = Column(Enum(SuscripcionCursoEnum), nullable=False)
    ubicacion = Column(String, nullable=True)

    def __init__(self, id_creador, titulo, descripcion, hashtags, tipo, examenes, suscripcion, ubicacion):
        self.id_creador = id_creador
        self.titulo = titulo
        self.descripcion = descripcion
        self.estado = EstadoCursoEnum.activo
        self.fecha_creacion = datetime.datetime.now()
        self.hashtags = hashtags
        self.tipo = tipo
        self.examenes = examenes
        self.suscripcion = suscripcion
        self.ubicacion = ubicacion

    def eliminar(self):
        self.estado = EstadoCursoEnum.eliminado
        self.actualizar()

    def getTitulo(self):
        return self.titulo

    def getDescripcion(self):
        return self.descripcion

    def getHashtags(self):
        return self.hashtags

    def getExamenes(self):
        return self.examenes

    def getUbicacion(self):
        return self.ubicacion

    def cambiarTitulo(self, nuevo_titulo):
        self.titulo = nuevo_titulo

    def cambiarDescripcion(self, nueva_descripcion):
        self.descripcion = nueva_descripcion

    def cambiarEstado(self, nuevo_estado):
        try:
            nuevoEstado = EstadoCursoEnum(nuevo_estado)
        except ValueError as e:
            raise HTTPException(status_code=400, detail='Debe proporcionar un estado válido: (' + str(e) + ')')
        self.estado = nuevoEstado

    def cambiarHashtags(self, nuevos_hashtags):
        self.hashtags = nuevos_hashtags

    def cambiarTipo(self, nuevo_tipo):
        try:
            nuevoTipo = TipoCursoEnum(nuevo_tipo)
        except ValueError as e:
            raise HTTPException(status_code=400, detail='Debe proporcionar un tipo válido: (' + str(e) + ')')
        self.tipo = nuevoTipo

    def cambiarExamenes(self, nuevos_examenes):
        self.examenes = nuevos_examenes

    def cambiarSuscripcion(self, nueva_suscripcion):
        try:
            nuevaSuscripcion = SuscripcionCursoEnum(nueva_suscripcion)
        except ValueError as e:
            raise HTTPException(status_code=400, detail='Debe proporcionar una suscripción válida: (' + str(e) + ')')
        self.suscripcion = nuevaSuscripcion

    def cambiarUbicacion(self, nueva_ubicacion):
        self.ubicacion = nueva_ubicacion

