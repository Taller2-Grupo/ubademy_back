import uuid

from sqlalchemy.orm import Session
from src.models.CursadaModel import Cursada
from src.schemas import CursadaSchema


def inscribir_alumno(curso_id: uuid.UUID, user: CursadaSchema.InscribirAlumno, db: Session):
    user.tiene_username(user.username)
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


def get_cursada(curso_id: uuid.UUID, user: CursadaSchema.InscribirAlumno, db: Session):
    return db.query(Cursada).filter(Cursada.curso_id == curso_id and Cursada.username == user.username).first()