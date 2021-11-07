import datetime
import enum
from sqlalchemy import Column, Enum, String
from sqlalchemy.dialects import postgresql
from src.models.Entity import Entity
from src.db.database import Base


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
    hashtags = Column(String, nullable=False)
    tipo = Column(Enum(TipoCursoEnum), nullable=False)
    examenes = Column(String, nullable=False)
    suscripcion = Column(Enum(SuscripcionCursoEnum), nullable=False)
    ubicacion = Column(String, nullable=False)

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

    def cambiarTitulo(self, nuevo_titulo):
        self.titulo = nuevo_titulo

    def cambiarDescripcion(self, nueva_descripcion):
        self.descripcion = nueva_descripcion

