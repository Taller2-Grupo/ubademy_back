import datetime
import enum
from sqlalchemy import Column, Enum, String
from sqlalchemy.dialects import postgresql
from src.models.Entity import Entity
from src.db.database import Base


class Cursada(Base, Entity):
    __tablename__ = "cursadas"
    username = Column(String, nullable=False)
    curso_id = Column(String, nullable=False)

    def __init__(self, username, curso_id):
        self.username = username
        self.curso_id = curso_id
        self.fecha_creacion = datetime.datetime.now()
