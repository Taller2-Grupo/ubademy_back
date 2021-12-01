import enum
# Este import sirve para relationship, no sacar.
from src.models.RespuestaModel import Respuesta

from sqlalchemy import Column, ForeignKey, String, Enum, INT
from sqlalchemy.dialects import postgresql
from sqlalchemy.orm import relationship
from src.models.Entity import Entity
from src.db.database import Base


class EstadoExamenResueltoEnum(str, enum.Enum):
    entregado = 'entregado'
    corregido = 'corregido'


class ExamenResuelto(Base, Entity):
    __tablename__ = "examenes_resueltos"
    id_cursada = Column(postgresql.UUID(as_uuid=True), ForeignKey('cursadas.id'))
    cursada = relationship("Cursada", back_populates="examenes_resueltos")
    id_examen = Column(postgresql.UUID(as_uuid=True), ForeignKey('examenes.id'))
    examen = relationship("Examen", back_populates="examenes_resueltos")
    corrector = Column(String, nullable=True)
    estado = Column(Enum(EstadoExamenResueltoEnum), nullable=False)
    nota = Column(INT, nullable=True)
    respuestas = relationship("Respuesta", back_populates="examen_resuelto", cascade="all, delete-orphan")

    def __init__(self, id_cursada, id_examen, respuestas):
        self.id_cursada = id_cursada
        self.id_examen = id_examen
        self.estado = EstadoExamenResueltoEnum.entregado
        self.respuestas = []
        for respuesta in respuestas:
            self.respuestas.append(Respuesta(self.id, respuesta.consigna, respuesta.resolucion))
