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
