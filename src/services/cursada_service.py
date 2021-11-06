import uuid

from src.db.repositories import cursada_repository
from sqlalchemy.orm import Session
from fastapi import HTTPException
from src.schemas import CursadaSchema


def inscribir_alumno(curso_id: uuid.UUID, user: CursadaSchema.InscribirAlumno, db: Session):
    return cursada_repository.inscribir_alumno(curso_id, user, db)