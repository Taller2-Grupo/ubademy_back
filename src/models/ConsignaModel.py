# Este import es para relationship, no sacar.
# from src.models.ExamenModel import Examen

from sqlalchemy import Column, ForeignKey, String, INT
from sqlalchemy.dialects import postgresql
from sqlalchemy.orm import relationship

from src.models.Entity import Entity
from src.db.database import Base


class Consigna(Base, Entity):
    __tablename__ = "consignas"
    id_examen = Column(postgresql.UUID(as_uuid=True), ForeignKey('examenes.id'))
    examen = relationship("Examen", back_populates="consignas")
    enunciado = Column(String, nullable=False)
    puntaje = Column(INT, nullable=False)

    def __init__(self, id_examen, enunciado, puntaje):
        self.id_examen = id_examen
        self.enunciado = enunciado
        self.puntaje = puntaje
