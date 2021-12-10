import uuid

from sqlalchemy.orm import Session
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

