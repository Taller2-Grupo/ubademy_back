from fastapi import FastAPI, Depends, HTTPException
import uvicorn
from src.schemas import CursoSchema
from sqlalchemy.orm import Session
from src.db.database import get_db
from src.db.crud import crud_curso

api = FastAPI()


@api.get('/')
async def index():
    return {
        "message": "Hello World!",
        "status": "OK"
    }


@api.post('/curso')
def crear_curso(curso: CursoSchema.CursoBase):
    return curso


@api.post("/cursos/", response_model=CursoSchema.Curso)
def create_curso(curso: CursoSchema.CursoCreate, db: Session = Depends(get_db)):
    return crud_curso.create_curso(db=db, curso=curso)


@api.get("/cursos/{curso_id}", response_model=CursoSchema.Curso)
def read_user(curso_id: int, db: Session = Depends(get_db)):
    db_user = crud_curso.get_curso(db, curso_id=curso_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@api.get('/users')
def get_hardcoded_user():
    return {
        "user": "pedro123!",
        "password": "123456"
    }

uvicorn.run(api)
