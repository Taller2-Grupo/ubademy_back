import decimal

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.db.database import get_db
from src.schemas import CursoSchema
from src.services import recomendacion_service
from typing import List

router = APIRouter(
    prefix="/recomendaciones",
    tags=["recomendaciones"]
)


@router.get("/intereses/{username}", response_model=List[CursoSchema.CursoResponse])
def get_recomendacion_por_intereses(username: str, db: Session = Depends(get_db)):
    return recomendacion_service.recomendar_curso_por_intereses(db, username)


@router.get("/ubicacion/{username}/{latitud}/{longitud}", response_model=List[CursoSchema.CursoResponse])
def get_recomendacion_por_intereses(
        username: str,
        latitud: decimal.Decimal,
        longitud: decimal.Decimal,
        db: Session = Depends(get_db)):
    return recomendacion_service.recomendar_cursos_por_ubicacion(db, username, latitud, longitud)
