import uuid
from src.db.repositories import cursada_repository
from sqlalchemy.orm import Session
from fastapi import HTTPException
from src.schemas import CursadaSchema


def inscribir_alumno(curso_id: uuid.UUID, user: CursadaSchema.InscribirAlumno, db: Session):
    # TODO: Validar que el username sea válido.
    return cursada_repository.inscribir_alumno(curso_id, user, db)


def get_cursada(curso_id: uuid.UUID, user: CursadaSchema.InscribirAlumno, db: Session):
    db_cursada = cursada_repository.get_cursada(curso_id, user, db)
    if db_cursada is None:
        raise HTTPException(status_code=404, detail="Cursada not found")
    return db_cursada


def desinscribir_alumno(curso_id: uuid.UUID, user: CursadaSchema.InscribirAlumno, db: Session):
    db_cursada = get_cursada(curso_id, user, db)
    db_cursada.cambiarEstadoADesinscripto()
    return cursada_repository.actualizar_cursada(db, db_cursada)
