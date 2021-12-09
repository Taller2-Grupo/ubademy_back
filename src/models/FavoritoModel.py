from alembic.ddl import postgresql
from sqlalchemy import Column, String
from src.models.Entity import Entity
from src.db.database import Base
from sqlalchemy.dialects import postgresql
import uuid


class Favorito(Base):
    __tablename__ = "favoritos"
    username = Column(String, nullable=False, primary_key=True)
    curso_id = Column(String, nullable=False, primary_key=True)

    def __init__(self, username, curso_id):
        self.username = username
        self.curso_id = curso_id
