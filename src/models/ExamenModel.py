import enum
# Este import de Consigna sirve para relationship, no sacar.
from src.models.ConsignaModel import Consigna

from sqlalchemy import Column, ForeignKey, String, Enum
from sqlalchemy.dialects import postgresql
from sqlalchemy.orm import relationship
from src.models.Entity import Entity
from src.db.database import Base


class EstadoExamenEnum(str, enum.Enum):
    creado = 'creado'
    publicado = 'publicado'


class Examen(Base, Entity):
    __tablename__ = "examenes"
    id_curso = Column(postgresql.UUID(as_uuid=True), ForeignKey('cursos.id'))
    curso = relationship("Curso", back_populates="examenes")
    nombre = Column(String, nullable=False)
    estado = Column(Enum(EstadoExamenEnum), nullable=False)
    consignas = relationship("Consigna", back_populates="examen", cascade="all, delete-orphan")

    def __init__(self, id_curso, nombre, consignas):
        self.id_curso = id_curso
        self.nombre = nombre
        self.estado = EstadoExamenEnum.creado
        self.consignas = []
        for consigna in consignas:
            self.consignas.append(Consigna(self.id, consigna))
