import uuid

from fastapi import FastAPI, Depends, Query

from src.schemas import CursoSchema, CursadaSchema
from sqlalchemy.orm import Session
from src.db.database import get_db
from src.services import curso_service, cursada_service
from src.models.CursoModel import EstadoCursoEnum, TipoCursoEnum
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
def get_cursos_by_estado(estados: Optional[List[EstadoCursoEnum]] = Query(None, alias="estado"), db: Session = Depends(get_db)):
    return curso_service.get_cursos(estados, db)


@app.get("/cursos/tipos/", response_model=List[CursoSchema.CursoResponse])
def get_cursos_by_tipo(tipos: Optional[List[TipoCursoEnum]] = Query(None, alias="tipo"), db: Session = Depends(get_db)):
    return curso_service.get_cursos_by_tipo_curso(tipos, db)


@app.put("/cursos/{curso_id}", response_model=CursoSchema.CursoResponse)
def editar_curso(curso_id: uuid.UUID, curso: CursoSchema.EditarCurso, db: Session = Depends(get_db)):
    return curso_service.editar_curso(curso_id=curso_id, curso=curso, db=db)


@app.get("/{creador_id}/cursos", response_model=List[CursoSchema.CursoResponse])
def get_cursos_creador(creador_id: uuid.UUID, db: Session = Depends(get_db)):
    return curso_service.get_cursos_creador(creador_id, db)


@app.post("/cursos/{curso_id}/inscribirse", response_model=CursadaSchema.CursadaResponse)
def inscribir_alumno(curso_id: uuid.UUID, user: CursadaSchema.InscribirAlumno, db: Session = Depends(get_db)):
    return cursada_service.inscribir_alumno(curso_id, user, db)


@app.put("/cursos/{curso_id}/desinscribirse", response_model=CursadaSchema.CursadaResponse)
def desinscribir_alumno(curso_id: uuid.UUID, user: CursadaSchema.InscribirAlumno, db: Session = Depends(get_db)):
    return cursada_service.desinscribir_alumno(curso_id, user, db)


@app.get("/cursos/{curso_id}/alumnos", response_model=List[str])
def get_listado_alumnos_curso(curso_id: uuid.UUID, db: Session = Depends(get_db)):
    return curso_service.get_listado_alumnos(curso_id, db)