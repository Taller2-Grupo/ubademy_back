import uuid
import enum
from sqlalchemy import Column, Enum, String
from sqlalchemy.dialects import postgresql

from src.db.database import Base


class EstadoCursoEnum(str, enum.Enum):
    activo = 'activo'
    bloqueado = 'bloqueado'
    eliminado = 'eliminado'


class Curso(Base):
    __tablename__ = "cursos"
    id = Column(postgresql.UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    id_creador = Column(postgresql.UUID(as_uuid=True), nullable=False, index=True)
    titulo = Column(String, nullable=False)
    descripcion = Column(String, nullable=False)
    estado = Column(Enum(EstadoCursoEnum), nullable=False)
