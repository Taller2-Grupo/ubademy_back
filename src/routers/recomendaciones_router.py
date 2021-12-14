from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from src.db.database import get_db
from src.services import recomendacion_service

router = APIRouter(
    prefix="/recomendaciones",
    tags=["recomendaciones"]
)


@router.get("/intereses")
def get_recomendacion_por_intereses(username: str, db: Session = Depends(get_db)):
    return recomendacion_service.recomendar_curso_por_intereses(db, username)
