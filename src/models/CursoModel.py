from sqlalchemy import Column, Integer, String

from src.db.database import Base


class Curso(Base):
    __tablename__ = "cursos"
    id = Column(Integer, primary_key=True, index=True)
    cantidad_alumnos = Column(Integer, nullable=False)
    cantidad_condicionales = Column(Integer, nullable=False)
    nombre = Column(String, nullable=False)