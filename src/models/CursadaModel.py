import datetime
import enum

from sqlalchemy import Column, Enum, String
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

    def __init__(self, username, curso_id):
        self.username = username
        self.curso_id = curso_id
        self.fecha_creacion = datetime.datetime.now()
        self.estado = EstadoCursadaEnum.inscripto

    def cambiarEstadoADesinscripto(self):
        self.estado = self.estado.desinscripto

    def cambiarEstadoAInscripto(self):
        self.estado = self.estado.inscripto
