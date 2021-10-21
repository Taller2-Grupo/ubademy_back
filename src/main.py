import uuid

from fastapi import FastAPI, Depends, Query

from src.models.AlumnoModel import Alumno
from src.schemas import CursoSchema
from sqlalchemy.orm import Session
from src.db.database import get_db
from src.services import curso_service
from src.models.CursoModel import EstadoCursoEnum
from typing import Optional, List

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/cursos/", response_model=CursoSchema.CursoResponse)
def create_curso(curso: CursoSchema.CreateCursoRequest, db: Session = Depends(get_db)):
    return curso_service.crear_curso(curso=curso, db=db)


@app.get("/cursos/{curso_id}", response_model=CursoSchema.CursoResponse)
def get_curso(curso_id: uuid.UUID, db: Session = Depends(get_db)):
    return curso_service.get_curso(curso_id, db)

@app.delete("/cursos/{curso_id}", response_model=CursoSchema.CursoResponse)
def delete_curso(curso_id: uuid.UUID, db: Session = Depends(get_db)):
    return curso_service.eliminar_curso(curso_id, db)


@app.get("/cursos", response_model=List[CursoSchema.CursoResponse])
def get_cursos(estados: Optional[List[EstadoCursoEnum]] = Query(None, alias="estado"), db: Session = Depends(get_db)):
    return curso_service.get_cursos(estados, db)

@app.get("/cursos/{curso_id}/alumnos", response_model=CursoSchema.CursoResponse)
def get_listado_alumnos_curso(curso_id: uuid.UUID, db: Session = Depends(get_db)):
    return curso_service.get_listado_alumnos_curso(curso_id, db)

@app.post("/cursos/{curso_id}", response_model=CursoSchema.CursoResponse)
def agregar_alumno_curso(curso_id: uuid.UUID, alumno: Alumno, db: Session = Depends(get_db)):
    curso = curso_service.get_curso(curso_id, db)
    curso.agregarAlumno(alumno)
