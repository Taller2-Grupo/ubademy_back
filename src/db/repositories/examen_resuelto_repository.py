import uuid

from sqlalchemy.orm import Session

from src.models.CursadaModel import Cursada
from src.models.ExamenResueltoModel import ExamenResuelto
from src.schemas import ExamenResueltoSchema


def create_examen_resuelto(
        db: Session,
        examen_resuelto: ExamenResueltoSchema.CreateExamenResueltoRequest,
        id_cursada: uuid.UUID):
    db_examen = ExamenResuelto(id_cursada, examen_resuelto.id_examen, examen_resuelto.respuestas)
    db.add(db_examen)
    db.commit()
    db.refresh(db_examen)
    return db_examen


def get_examen_resuelto_by_id(db: Session, id_examen_resuelto: uuid.UUID):
    return db.query(ExamenResuelto).filter(ExamenResuelto.id == id_examen_resuelto).first()


def actualizar_examen_resuelto(db: Session, examen_resuelto: ExamenResuelto):
    db.add(examen_resuelto)
    db.commit()
    db.refresh(examen_resuelto)
    return examen_resuelto


def get_examenes_resueltos_by_curso(db, curso_id, estados):
    examenes_by_curso = db.query(ExamenResuelto).join(Cursada).filter(Cursada.curso_id == curso_id)
    if estados is None:
        return examenes_by_curso.all()
    return examenes_by_curso.filter(ExamenResuelto.estado.in_(estados)).all()


def get_examenes_resueltos_by_curso_and_username(db, curso_id, username, estados):
    examenes_by_curso = \
        db.query(ExamenResuelto).join(Cursada).filter(Cursada.curso_id == curso_id).filter(Cursada.username == username)

    if estados is None:
        return examenes_by_curso.all()

    return examenes_by_curso.filter(ExamenResuelto.estado.in_(estados)).all()
