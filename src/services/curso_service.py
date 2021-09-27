import uuid

from src.db.repositories import curso_repository
from sqlalchemy.orm import Session
from fastapi import HTTPException
from src.schemas import CursoSchema


def crear_curso(curso: CursoSchema.CreateCursoRequest, db: Session):
    return curso_repository.create_curso(db=db, curso=curso)


def get_curso(curso_id: uuid.UUID, db: Session):
    db_curso = curso_repository.get_curso(db, curso_id=curso_id)
    if db_curso is None:
        raise HTTPException(status_code=404, detail="Curso not found")
    return db_curso


def eliminar_curso(curso_id: uuid.UUID, db: Session):
    db_curso = get_curso(curso_id, db)
    db_curso.eliminar()