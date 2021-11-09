import uuid

from sqlalchemy.orm import Session

from src.models.CursadaModel import Cursada, EstadoCursadaEnum
from src.models.CursoModel import Curso, EstadoCursoEnum
from src.schemas import CursoSchema
from typing import List, Optional
from fastapi import HTTPException


def get_curso(db: Session, curso_id: uuid.UUID):
    return db.query(Curso).filter(Curso.id == curso_id).first()


def get_cursos_creador(db: Session, creador_id: uuid.UUID):
    cursos = []
    for curso in db.query(Curso):
        if str(curso.id_creador) == str(creador_id):
            cursos.append(curso)
    return cursos


def create_curso(db: Session, curso: CursoSchema.CreateCursoRequest):
    curso.tiene_titulo(curso.titulo)
    curso.tiene_descripcion(curso.descripcion)
    curso.tiene_tipo(curso.tipo)
    curso.tiene_suscripcion(curso.suscripcion)
    db_curso = Curso(
        curso.id_creador,
        curso.titulo,
        curso.descripcion,
        curso.hashtags,
        curso.tipo,
        curso.examenes,
        curso.suscripcion,
        curso.ubicacion
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

def get_listado_alumnos(curso_id: uuid.UUID, db: Session):
    cursadas = db.query(Cursada).filter(Cursada.curso_id == curso_id, Cursada.estado == EstadoCursadaEnum.inscripto).all()
    listado = []
    for cursada in cursadas:
        listado.append(cursada.username)
    return listado
