import string
import uuid
from typing import List, Optional

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from src.db.database import get_db
from src.models.CursoModel import EstadoCursoEnum, TipoCursoEnum, SuscripcionCursoEnum
from src.schemas import CursoSchema, ExamenSchema, ColaboradorSchema, CursadaSchema, ExamenResueltoSchema
from src.services import curso_service, cursada_service

router = APIRouter(
    prefix="/cursadas",
    tags=["cursadas"]
)


@router.get("/{username}/", response_model=List[CursoSchema.CursoResponse])
def get_cursadas(username: string, db: Session = Depends(get_db)):
    return cursada_service.get_cursadas(username=username, db=db)
