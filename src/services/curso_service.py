import uuid

from src.db.repositories import curso_repository
from sqlalchemy.orm import Session
from fastapi import HTTPException
from src.schemas import CursoSchema
from src.models.CursoModel import EstadoCursoEnum
from typing import List, Optional


def crear_curso(curso: CursoSchema.CreateCursoRequest, db: Session):
    return curso_repository.create_curso(db=db, curso=curso)

def get_curso(curso_id: uuid.UUID, db: Session):
    db_curso = curso_repository.get_curso(db, curso_id=curso_id)
    if db_curso is None:
        raise HTTPException(status_code=404, detail="Curso not found")
    return db_curso

def get_cursos_creador(creador_id: uuid.UUID, db: Session):
    return curso_repository.get_cursos_creador(db, creador_id=creador_id)

def eliminar_curso(curso_id: uuid.UUID, db: Session):
    db_curso = get_curso(curso_id, db)
    db_curso.eliminar()
    return curso_repository.actualizar_curso(db, db_curso)

def editar_curso(curso_id: uuid.UUID, curso: CursoSchema.EditarCurso, db: Session):
    db_curso = get_curso(curso_id, db)
    if curso.nuevo_titulo:
        db_curso.cambiarTitulo(curso.nuevo_titulo)
    if curso.nueva_descripcion:
        db_curso.cambiarDescripcion(curso.nueva_descripcion)
    if curso.nuevo_estado:
        db_curso.cambiarEstado(curso.nuevo_estado)
    if curso.nuevos_hashtags:
        db_curso.cambiarHashtags(curso.nuevos_hashtags)
    if curso.nuevo_tipo:
        db_curso.cambiarTipo(curso.nuevo_tipo)
    if curso.nuevos_examenes:
        db_curso.cambiarExamenes(curso.nuevos_examenes)
    if curso.nueva_suscripcion:
        db_curso.cambiarSuscripcion(curso.nueva_suscripcion)
    if curso.nueva_ubicacion:
        db_curso.cambiarUbicacion(curso.nueva_ubicacion)
    return curso_repository.actualizar_curso(db, db_curso)

def get_cursos(estados: Optional[List[EstadoCursoEnum]], db: Session):
    return curso_repository.get_curso_by_estados(estados, db)

def get_listado_alumnos(curso_id: uuid.UUID, db: Session):
    get_curso(curso_id, db)
    return curso_repository.get_listado_alumnos(curso_id, db)
