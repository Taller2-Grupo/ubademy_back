import uuid

from fastapi import FastAPI, Depends, HTTPException
import uvicorn
from src.schemas import CursoSchema
from sqlalchemy.orm import Session
from src.db.database import get_db
from src.db.crud import crud_curso

api = FastAPI()


@api.post("/cursos/", response_model=CursoSchema.CursoResponse)
def create_curso(curso: CursoSchema.CreateCursoRequest, db: Session = Depends(get_db)):
    return crud_curso.create_curso(db=db, curso=curso)


@api.get("/cursos/{curso_id}", response_model=CursoSchema.CursoResponse)
def read_user(curso_id: uuid.UUID, db: Session = Depends(get_db)):
    db_user = crud_curso.get_curso(db, curso_id=curso_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


uvicorn.run(api)
