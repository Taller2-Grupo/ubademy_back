from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.dialects import postgresql
from sqlalchemy.orm import relationship
from src.models.Entity import Entity
from src.db.database import Base


class Colaborador(Base, Entity):
    __tablename__ = "colaboradores"
    id_curso = Column(postgresql.UUID(as_uuid=True), ForeignKey('cursos.id'))
    curso = relationship("Curso", back_populates="colaboradores")
    username = Column(String, nullable=False)

    def __init__(self, id_curso, username):
        self.id_curso = id_curso
        self.username = username
