import uuid
from typing import List, Optional

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from src.db.database import get_db
from src.models.ExamenModel import EstadoExamenEnum
from src.models.ExamenResueltoModel import EstadoExamenResueltoEnum
from src.schemas import ExamenSchema, ExamenResueltoSchema
from src.services import curso_service, cursada_service

router = APIRouter(
    prefix="/examenes",
    tags=["examenes"]
)


@router.post("", response_model=ExamenSchema.ExamenResponse, status_code=201)
def add_examen(examen: ExamenSchema.CreateExamenRequest, db: Session = Depends(get_db)):
    return curso_service.add_examen(examen, db)


@router.get("/{examen_id}", response_model=ExamenSchema.ExamenResponse)
def get_examen(examen_id: uuid.UUID, db: Session = Depends(get_db)):
    return curso_service.get_examen(examen_id, db)


@router.post("/publicar/{examen_id}", response_model=ExamenSchema.ExamenResponse)
def publicar_examen(examen_id: uuid.UUID, db: Session = Depends(get_db)):
    return curso_service.publicar_examen(examen_id, db)


@router.patch("", response_model=ExamenSchema.ExamenResponse)
def editar_examen(examen: ExamenSchema.EditExamenRequest, db: Session = Depends(get_db)):
    return curso_service.editar_examen(examen, db)


@router.post("/examenes_resueltos", response_model=ExamenResueltoSchema.ExamenResueltoResponse, status_code=201)
def add_examen_resuelto(
        examen_resuelto: ExamenResueltoSchema.CreateExamenResueltoRequest,
        db: Session = Depends(get_db)):
    return cursada_service.add_examen_resuelto(examen_resuelto, db)


@router.get("/curso/{curso_id}", response_model=List[ExamenSchema.ExamenResponse])
def get_examenes_by_curso(
        curso_id: uuid.UUID,
        estados: Optional[List[EstadoExamenEnum]] = Query(None, alias="estado"),
        db: Session = Depends(get_db)):
    return curso_service.get_examenes_by_curso(curso_id, estados, db)


@router.get("/examenes_resueltos/curso/{curso_id}", response_model=List[ExamenResueltoSchema.ExamenResueltoResponse])
def get_examenes_resueltos_by_curso(
        curso_id: uuid.UUID,
        estados: Optional[List[EstadoExamenResueltoEnum]] = Query(None, alias="estado"),
        db: Session = Depends(get_db)):
    return cursada_service.get_examenes_resueltos_by_curso(curso_id, estados, db)


@router.get("/examenes_resueltos/curso/{curso_id}/{username}", response_model=List[ExamenResueltoSchema.ExamenResueltoResponse])
def get_examenes_resueltos_by_curso_and_username(
        curso_id: uuid.UUID,
        username: str,
        estados: Optional[List[EstadoExamenResueltoEnum]] = Query(None, alias="estado"),
        db: Session = Depends(get_db)):
    return cursada_service.get_examenes_resueltos_by_curso_and_username(curso_id, username, estados, db)


@router.post("/examenes_resueltos/corregir", response_model=ExamenResueltoSchema.ExamenResueltoResponse, status_code=200)
def corregir_examen_resuelto(correccion: ExamenResueltoSchema.CorregirExamenRequest, db: Session = Depends(get_db)):
    return cursada_service.corregir_examen_resuelto(correccion, db)
