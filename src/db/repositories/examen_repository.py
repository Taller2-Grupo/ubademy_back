from sqlalchemy.orm import Session

from src.models.ExamenModel import Examen
from src.schemas import ExamenSchema


def create_examen(db: Session, examen: ExamenSchema.CreateExamenRequest):
    db_examen = Examen(examen.id_curso, examen.nombre, examen.consignas)
    db.add(db_examen)
    db.commit()
    db.refresh(db_examen)
    return db_examen
