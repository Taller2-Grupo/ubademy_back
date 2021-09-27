import uuid

from fastapi import FastAPI, Depends
import uvicorn
from src.schemas import CursoSchema
from sqlalchemy.orm import Session
from src.db.database import get_db
from src.services import curso_service

api = FastAPI()


@api.post("/cursos/", response_model=CursoSchema.CursoResponse)
def create_curso(curso: CursoSchema.CreateCursoRequest, db: Session = Depends(get_db)):
    return curso_service.crear_curso(curso=curso, db=db)


@api.get("/cursos/{curso_id}", response_model=CursoSchema.CursoResponse)
def get_curso(curso_id: uuid.UUID, db: Session = Depends(get_db)):
    return curso_service.get_curso(curso_id, db)


@api.delete("/cursos/{curso_id}", response_model=CursoSchema.CursoResponse)
def delete_curso(curso_id: uuid.UUID, db: Session = Depends(get_db)):
    return curso_service.eliminar_curso(curso_id, db)


uvicorn.run(api)
