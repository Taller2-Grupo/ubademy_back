import uuid

from sqlalchemy.orm import Session
from src.models.CursoModel import Curso, EstadoCursoEnum
from src.schemas import CursoSchema


def get_curso(db: Session, curso_id: uuid.UUID):
    return db.query(Curso).filter(Curso.id == curso_id).first()


def create_curso(db: Session, curso: CursoSchema.CreateCursoRequest):
    db_curso = Curso\
        (curso.id_creador,
         curso.titulo,
         curso.descripcion)
    db.add(db_curso)
    db.commit()
    db.refresh(db_curso)
    return db_curso

