import uuid

from sqlalchemy.orm import Session

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
