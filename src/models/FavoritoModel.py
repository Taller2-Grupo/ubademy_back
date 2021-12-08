from sqlalchemy import Column, String
from src.models.Entity import Entity
from src.db.database import Base


class Favorito(Base, Entity):
    __tablename__ = "favoritos"
    username = Column(String, nullable=False)
    curso_id = Column(String, nullable=False)

    def __init__(self, username, curso_id):
        self.username = username
        self.curso_id = curso_id
