import datetime
import enum
# Este import de Colaborador sirve para relationship, no sacar.
from src.models.ColaboradorModel import Colaborador
from src.models.ExamenModel import Examen

from sqlalchemy import Column, Enum, String, DECIMAL
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
    premium = 'premium'
    vip = 'vip'


class Curso(Base, Entity):
    __tablename__ = "cursos"
    id_creador = Column(String, nullable=False)
    titulo = Column(String, nullable=False)
    descripcion = Column(String, nullable=False)
    estado = Column(Enum(EstadoCursoEnum), nullable=False)
    hashtags = Column(String, nullable=True)
    tipo = Column(Enum(TipoCursoEnum), nullable=False)
    suscripcion = Column(Enum(SuscripcionCursoEnum), nullable=False)
    colaboradores = relationship("Colaborador", back_populates="curso")
    examenes = relationship("Examen", back_populates="curso")
    latitud = Column(DECIMAL, nullable=True)
    longitud = Column(DECIMAL, nullable=True)

    def __init__(self, id_creador, titulo, descripcion, hashtags, tipo, suscripcion, latitud=None, longitud=None):
        self.id_creador = id_creador
        self.titulo = titulo
        self.descripcion = descripcion
        self.estado = EstadoCursoEnum.activo
        self.fecha_creacion = datetime.datetime.now()
        self.hashtags = hashtags
        self.tipo = tipo
        self.suscripcion = suscripcion

        if latitud is not None and longitud is None:
            raise HTTPException(status_code=400, detail="El curso debe tener latitud y longitud o ninguna de las dos")

        if latitud is None and longitud is not None:
            raise HTTPException(status_code=400, detail="El curso debe tener latitud y longitud o ninguna de las dos")

        self.latitud = latitud
        self.longitud = longitud

    def eliminar(self):
        self.estado = EstadoCursoEnum.eliminado
        self.actualizar()

    def bloquear(self):
        if self.estado == EstadoCursoEnum.eliminado:
            raise HTTPException(status_code=400, detail='No se puede bloquear un curso eliminado')

        self.estado = EstadoCursoEnum.bloqueado
        self.actualizar()

    def activar(self):
        if self.estado == EstadoCursoEnum.eliminado:
            raise HTTPException(status_code=400, detail='No se puede activar un curso eliminado')

        self.estado = EstadoCursoEnum.activo
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

    def set_titulo(self, nuevo_titulo):
        self.titulo = nuevo_titulo

    def set_descripcion(self, nueva_descripcion):
        self.descripcion = nueva_descripcion

    def set_estado(self, nuevo_estado):
        try:
            nuevo_estado_enum = EstadoCursoEnum(nuevo_estado)
        except ValueError as e:
            raise HTTPException(status_code=400, detail='Debe proporcionar un estado v??lido: (' + str(e) + ')')
        self.estado = nuevo_estado_enum

    def set_hashtags(self, nuevos_hashtags):
        self.hashtags = nuevos_hashtags

    def set_tipo(self, nuevo_tipo):
        try:
            nuevo_tipo_enum = TipoCursoEnum(nuevo_tipo)
        except ValueError as e:
            raise HTTPException(status_code=400, detail='Debe proporcionar un tipo v??lido: (' + str(e) + ')')
        self.tipo = nuevo_tipo_enum

    def set_suscripcion(self, nueva_suscripcion):
        try:
            nueva_suscripcion_enum = SuscripcionCursoEnum(nueva_suscripcion)
        except ValueError as e:
            raise HTTPException(status_code=400, detail='Debe proporcionar una suscripci??n v??lida: (' + str(e) + ')')
        self.suscripcion = nueva_suscripcion_enum

    def set_latitud_and_longitud(self, latitud, longitud):
        if latitud is None and longitud is not None:
            raise HTTPException(status_code=400, detail="El curso debe tener latitud y longitud o ninguna de las dos")

        if longitud is None and latitud is not None:
            raise HTTPException(status_code=400, detail="El curso debe tener latitud y longitud o ninguna de las dos")

        self.latitud = latitud
        self.longitud = longitud
        self.actualizar()
