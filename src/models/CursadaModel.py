# Este import sirve para relationship, no sacar.
from src.models.ExamenResueltoModel import ExamenResuelto

import datetime
import enum

from sqlalchemy import Column, Enum, String
from sqlalchemy.orm import relationship

from src.models.Entity import Entity
from src.db.database import Base
from sqlalchemy.dialects.postgresql import UUID
import uuid


class EstadoCursadaEnum(str, enum.Enum):
    inscripto = 'inscripto'
    solicitado_de_alta = 'solicitado_de_alta'
    solicitado_de_baja = 'solicitado_de_baja'
    desinscripto = 'desinscripto'


class Cursada(Base, Entity):
    __tablename__ = "cursadas"
    username = Column(String, nullable=False)
    curso_id = Column(UUID(as_uuid=True), default=uuid.uuid4)
    estado = Column(Enum(EstadoCursadaEnum), nullable=False)
    examenes_resueltos = relationship("ExamenResuelto", back_populates="cursada")

    def __init__(self, username, curso_id):
        self.username = username
        self.curso_id = curso_id
        self.fecha_creacion = datetime.datetime.now()
        self.estado = EstadoCursadaEnum.inscripto

    def cambiar_estado_a_desinscripto(self):
        self.estado = EstadoCursadaEnum.desinscripto

    def cambiar_estado_a_inscripto(self):
        self.estado = EstadoCursadaEnum.inscripto
