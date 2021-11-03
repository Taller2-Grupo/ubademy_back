import uuid

from sqlalchemy.orm import Session
from src.models.CursoModel import Curso, EstadoCursoEnum
from src.schemas import CursoSchema
from typing import List, Optional


def get_curso(db: Session, curso_id: uuid.UUID):
    return db.query(Curso).filter(Curso.id == curso_id).first()

def get_cursos_creador(db: Session, creador_id: uuid.UUID):
    cursos = []
    for curso in db.query(Curso):
        if curso.id_creador == creador_id:
            cursos.append(curso)
    return cursos

def create_curso(db: Session, curso: CursoSchema.CreateCursoRequest):
    db_curso = Curso(
        curso.id_creador,
        curso.titulo,
        curso.descripcion
    )
    db.add(db_curso)
    db.commit()
    db.refresh(db_curso)
    return db_curso


def actualizar_curso(db: Session, curso: Curso):
    db.add(curso)
    db.commit()
    db.refresh(curso)
    return curso


def get_curso_by_estados(estados: Optional[List[EstadoCursoEnum]], db: Session):
    if estados is None:
        return db.query(Curso).all()
    return db.query(Curso).filter(Curso.estado.in_(estados)).all()
