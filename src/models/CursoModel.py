import datetime
import enum
# Este import de Colaborador sirve para relationship, no sacar.
from src.models.ColaboradorModel import Colaborador

from sqlalchemy import Column, Enum, String
from sqlalchemy.orm import relationship

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
    suscripcion = Column(Enum(SuscripcionCursoEnum), nullable=False)
    ubicacion = Column(String, nullable=True)
    colaboradores = relationship("Colaborador", back_populates="curso")
    examenes = relationship("Examen", back_populates="curso")

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

    def get_titulo(self):
        return self.titulo

    def get_descripcion(self):
        return self.descripcion

    def get_estado(self):
        return self.estado.value

    def get_hashtags(self):
        return self.hashtags

    def get_tipo(self):
        return self.tipo.value

    def get_examenes(self):
        return self.examenes

    def get_suscripcion(self):
        return self.suscripcion.value

    def get_ubicacion(self):
        return self.ubicacion

    def set_titulo(self, nuevo_titulo):
        self.titulo = nuevo_titulo

    def set_descripcion(self, nueva_descripcion):
        self.descripcion = nueva_descripcion

    def set_estado(self, nuevo_estado):
        try:
            nuevo_estado_enum = EstadoCursoEnum(nuevo_estado)
        except ValueError as e:
            raise HTTPException(status_code=400, detail='Debe proporcionar un estado válido: (' + str(e) + ')')
        self.estado = nuevo_estado_enum

    def set_hashtags(self, nuevos_hashtags):
        self.hashtags = nuevos_hashtags

    def set_tipo(self, nuevo_tipo):
        try:
            nuevo_tipo_enum = TipoCursoEnum(nuevo_tipo)
        except ValueError as e:
            raise HTTPException(status_code=400, detail='Debe proporcionar un tipo válido: (' + str(e) + ')')
        self.tipo = nuevo_tipo_enum

    def set_examenes(self, nuevos_examenes):
        self.examenes = nuevos_examenes

    def set_suscripcion(self, nueva_suscripcion):
        try:
            nueva_suscripcion_enum = SuscripcionCursoEnum(nueva_suscripcion)
        except ValueError as e:
            raise HTTPException(status_code=400, detail='Debe proporcionar una suscripción válida: (' + str(e) + ')')
        self.suscripcion = nueva_suscripcion_enum

    def set_ubicacion(self, nueva_ubicacion):
        self.ubicacion = nueva_ubicacion

