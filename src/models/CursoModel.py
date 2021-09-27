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


class Curso(Base, Entity):
    __tablename__ = "cursos"
    id_creador = Column(postgresql.UUID(as_uuid=True), nullable=False, index=True)
    titulo = Column(String, nullable=False)
    descripcion = Column(String, nullable=False)
    estado = Column(Enum(EstadoCursoEnum), nullable=False)

    def __init__(self, id_creador, titulo, descripcion):
        self.id_creador = id_creador
        self.titulo = titulo
        self.descripcion = descripcion
        self.estado = EstadoCursoEnum.activo
        self.fecha_creacion = datetime.datetime.now()

    def eliminar(self):
        self.estado = EstadoCursoEnum.eliminado
        self.actualizar()
