import datetime
import enum
from sqlalchemy import Column, Enum, String
from sqlalchemy.dialects import postgresql
from src.models.Entity import Entity
from src.db.database import Base

class Alumno(Base, Entity):
    __tablename__ = "alumnos"
    nombre = Column(String, nullable=False)
    apellido = Column(String, nullable=False)
    padron = Column(String, nullable=False)

    def __init__(self, nombre, apellido, padron):
        self.nombre = nombre
        self.apellido = apellido
        self.padron = padron