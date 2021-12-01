# Este import es para relationship, no sacar.
# from src.models.ExamenResueltoModel import ExamenResuelto
import enum

from sqlalchemy import Column, ForeignKey, String, Enum
from sqlalchemy.dialects import postgresql
from sqlalchemy.orm import relationship

from src.models.Entity import Entity
from src.db.database import Base


class EstadoRespuestaEnum(str, enum.Enum):
    sin_corregir = 'sin corregir'
    correcta = 'correcta'
    incorrecta = 'incorrecta'


class Respuesta(Base, Entity):
    __tablename__ = "respuestas"
    id_examen_resuelto = Column(postgresql.UUID(as_uuid=True), ForeignKey('examenes_resueltos.id'))
    examen_resuelto = relationship("ExamenResuelto", back_populates="respuestas")
    consigna = Column(String, nullable=False)
    resolucion = Column(String, nullable=False)
    estado = Column(Enum(EstadoRespuestaEnum), nullable=False)

    def __init__(self, id_examen_resuelto, consigna, resolucion):
        self.id_examen_resuelto = id_examen_resuelto
        self.consigna = consigna
        self.resolucion = resolucion
        self.estado = EstadoRespuestaEnum.sin_corregir
