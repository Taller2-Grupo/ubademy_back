from sqlalchemy.orm import Session
from src.models.CursoModel import Curso
from src.schemas import CursoSchema


def get_curso(db: Session, curso_id: int):
    return db.query(Curso).filter(Curso.id == curso_id).first()


def create_curso(db: Session, curso: CursoSchema.CursoCreate):
    db_curso = Curso\
        (cantidad_alumnos=curso.cantidad_alumnos,
         cantidad_condicionales=curso.cantidad_condicionales,
         nombre=curso.nombre)
    db.add(db_curso)
    db.commit()
    db.refresh(db_curso)
    return db_curso

