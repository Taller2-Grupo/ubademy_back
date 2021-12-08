import uuid
from typing import List, Optional

from sqlalchemy.orm import Session
from src.models.ExamenModel import Examen, EstadoExamenEnum
from src.schemas import ExamenSchema


def get_examen(db: Session, examen_id: uuid.UUID):
    return db.query(Examen).filter(Examen.id == examen_id).first()


def actualizar_examen(db: Session, examen: Examen):
    db.add(examen)
    db.commit()
    db.refresh(examen)
    return examen


def create_examen(db: Session, examen: ExamenSchema.CreateExamenRequest):
    db_examen = Examen(examen.id_curso, examen.nombre, examen.consignas)
    db.add(db_examen)
    db.commit()
    db.refresh(db_examen)
    return db_examen


def get_examenes_by_curso(db: Session, curso_id: uuid.UUID, estados: Optional[List[EstadoExamenEnum]]):
    examenes_by_curso = db.query(Examen).filter(Examen.id_curso == curso_id)
    if estados is None:
        return examenes_by_curso.all()
    return examenes_by_curso.filter(Examen.estado.in_(estados)).all()
