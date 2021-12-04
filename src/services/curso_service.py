import uuid

from src.db.repositories import curso_repository, colaborador_repository, examen_repository
from sqlalchemy.orm import Session
from fastapi import HTTPException

from src.models.ConsignaModel import Consigna
from src.models.ExamenModel import EstadoExamenEnum
from src.schemas import CursoSchema, ColaboradorSchema, ExamenSchema
from src.models.CursoModel import EstadoCursoEnum, TipoCursoEnum, SuscripcionCursoEnum
from typing import List, Optional


def crear_curso(curso: CursoSchema.CreateCursoRequest, db: Session):
    # TODO: Validar que el username es válido.
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
        db_curso.set_titulo(curso.nuevo_titulo)
    if curso.nueva_descripcion:
        db_curso.set_descripcion(curso.nueva_descripcion)
    if curso.nuevo_estado:
        db_curso.set_estado(curso.nuevo_estado)
    if curso.nuevos_hashtags:
        db_curso.set_hashtags(curso.nuevos_hashtags)
    if curso.nuevo_tipo:
        db_curso.set_tipo(curso.nuevo_tipo)
    if curso.nueva_suscripcion:
        db_curso.set_suscripcion(curso.nueva_suscripcion)
    if curso.nueva_ubicacion:
        db_curso.set_ubicacion(curso.nueva_ubicacion)
    return curso_repository.actualizar_curso(db, db_curso)


def get_cursos(estados: Optional[List[EstadoCursoEnum]], db: Session):
    return curso_repository.get_curso_by_estados(estados, db)


def get_cursos_by_tipo_curso(tipos: Optional[List[TipoCursoEnum]], db: Session):
    return curso_repository.get_curso_by_tipo_curso(tipos, db)


def get_cursos_by_suscripcion(suscripciones: Optional[List[SuscripcionCursoEnum]], db: Session):
    return curso_repository.get_curso_by_suscripcion(suscripciones, db)


def get_listado_alumnos(curso_id: uuid.UUID, db: Session):
    get_curso(curso_id, db)
    return curso_repository.get_listado_alumnos(curso_id, db)


def add_colaborador(colaborador: ColaboradorSchema.CreateColaboradorRequest, db: Session):
    curso = get_curso(colaborador.id_curso, db)

    for c in curso.colaboradores:
        if c.username == colaborador.username:
            raise HTTPException(status_code=422, detail="El colaborador ya se encuentra dado de alta en el curso.")

    # TODO: Validar que el username es válido.

    colaborador_db = colaborador_repository.create_colaborador(db=db, colaborador=colaborador)

    curso.actualizar()
    curso_repository.actualizar_curso(db, curso)

    return colaborador_db


def add_examen(examen: ExamenSchema.CreateExamenRequest, db: Session):
    curso = get_curso(examen.id_curso, db)

    validar_consignas(examen.consignas)

    examen_db = examen_repository.create_examen(db=db, examen=examen)

    curso.actualizar()
    curso_repository.actualizar_curso(db, curso)

    return examen_db


def validar_consignas(consignas):
    puntaje_total: int = 0
    for consigna in consignas:
        puntaje_total += consigna.puntaje
    if puntaje_total != 10:
        raise HTTPException(status_code=400, detail="El puntaje de las consignas debe sumar 10.")


def get_examen(examen_id: uuid.UUID, db: Session):
    db_examen = examen_repository.get_examen(db, examen_id=examen_id)
    if db_examen is None:
        raise HTTPException(status_code=404, detail="Examen not found")
    return db_examen


def publicar_examen(id_examen: uuid.UUID, db: Session):
    examen = get_examen(id_examen, db)

    if examen.estado == EstadoExamenEnum.publicado:
        raise HTTPException(status_code=400, detail="El examen ya se encuentra publicado.")

    examen.estado = EstadoExamenEnum.publicado

    examen.actualizar()
    examen_repository.actualizar_examen(db, examen)

    return examen


def editar_examen(examen: ExamenSchema.EditExamenRequest, db: Session):
    examen_db = get_examen(examen.id, db)

    if examen_db.estado == EstadoExamenEnum.publicado:
        raise HTTPException(status_code=400, detail="No se puede editar un examen publicado.")

    validar_consignas(examen.consignas)

    examen_db.nombre = examen.nombre
    examen_db.consignas = []
    for consigna in examen.consignas:
        examen_db.consignas.append(Consigna(examen_db.id, consigna.enunciado, consigna.puntaje))

    examen_db.actualizar()
    examen_repository.actualizar_examen(db, examen_db)

    return examen_db


def get_examenes_by_curso(curso_id: uuid.UUID, db: Session):
    return examen_repository.get_examenes_by_curso(db, curso_id)
