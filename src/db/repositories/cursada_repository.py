import uuid
from typing import List

from sqlalchemy.orm import Session
from sqlalchemy.sql import text
from src.models.CursadaModel import Cursada, EstadoCursadaEnum
from src.models.CursoModel import Curso
from src.schemas import CursadaSchema
from fastapi import HTTPException


def inscribir_alumno(curso_id: uuid.UUID, user: CursadaSchema.InscribirAlumno, db: Session):
    user.tiene_username(user.username)
    cursada = get_cursada(curso_id, user.username, db)
    if cursada:
        if cursada.estado == EstadoCursadaEnum.inscripto:
            raise HTTPException(status_code=400,
                                detail="El alumno " + user.username + " ya se encuentra inscripto al curso " + str(
                                    curso_id))
        else:
            cursada.cambiar_estado_a_inscripto()
            return actualizar_cursada(db, cursada)
    else:
        db_cursada = Cursada(
            user.username,
            curso_id
        )
        db.add(db_cursada)
        db.commit()
        db.refresh(db_cursada)
        return db_cursada


def actualizar_cursada(db: Session, cursada: Cursada):
    db.add(cursada)
    db.commit()
    db.refresh(cursada)
    return cursada


def get_cursada(curso_id: uuid.UUID, username: str, db: Session):
    return db.query(Cursada).filter(Cursada.curso_id == curso_id, Cursada.username == username).first()


def get_cursada_by_id(cursada_id: uuid.UUID, db: Session):
    return db.query(Cursada).filter(Cursada.id == cursada_id).first()


def actualizar_cursada(db: Session, cursada: Cursada):
    db.add(cursada)
    db.commit()
    db.refresh(cursada)
    return cursada


def get_historicos(username, db):
    id_cursos = db.query(Cursada).filter(Cursada.username == username).with_entities(Cursada.curso_id).all()
    id_cursos_string = []
    for curso_id in id_cursos:
        id_cursos_string.append(str(curso_id)[7:43])
    return db.query(Curso).filter(Curso.id.in_(id_cursos_string)).all()


def get_cursos_mas_inscriptos_by_tipo_curso(db: Session, tipo_curso: str, ids_curso: List[str]):
    statement = text(
        """ select cursos.*, count(cursos.id) as cantidad_inscriptos from cursadas
            inner join cursos on cursos.id = cursadas.curso_id
            where cursos.tipo = :tipo_curso
            and cursos.estado = 'activo'
            and cursos.id not in :ids_curso
            group by cursos.id
            order by cantidad_inscriptos desc
            limit 10 """)

    params = {
        "tipo_curso": tipo_curso
    }

    statement = statement.bindparams(ids_curso=tuple(ids_curso))

    return db.execute(statement, params).all()


def get_cursos_mas_inscriptos(db: Session):
    statement = text(
        """ select cursos.*, count(cursos.id) as cantidad_inscriptos from cursadas
            inner join cursos on cursos.id = cursadas.curso_id
            where cursos.estado = 'activo'
            group by cursos.id
            order by cantidad_inscriptos desc
            limit 10 """)

    return db.execute(statement).all()


# def get_cursos_virtuales_con_mas_inscriptos(db: Session):
#     statement = text(
#         """ select cursos, count(cursos.id) as cantidad_inscriptos from cursadas
#             inner join cursos on cursos.id = cursadas.curso_id
#             where cursos.latitud is null and cursos.longitud is null
#             group by cursos.id
#             order by cantidad_inscriptos desc
#             limit 10 """)
#
#     return db.execute(statement).all()


def get_cursos_by_cercania(db: Session, username, latitud, longitud):
    statement = text(
        """ select
            *,
            SQRT(
                POW(69.1 * (cursos.latitud - :latitud), 2) +
                POW(69.1 * (:longitud - cursos.longitud) * COS(cursos.latitud / 57.3), 2)) as distance
            from cursos
            where
             SQRT(
                POW(69.1 * (cursos.latitud - :latitud), 2) +
                POW(69.1 * (:longitud - cursos.longitud) * COS(cursos.latitud / 57.3), 2)) < 2
            and estado = 'activo'
            and id_creador != :username
            order by distance
            limit 10 """)

    params = {
        "latitud": latitud,
        "longitud": longitud,
        "username": username
    }

    return db.execute(statement, params).all()
