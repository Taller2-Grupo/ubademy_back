import uuid
from typing import List, Optional

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from src.db.database import get_db
from src.models.CursoModel import EstadoCursoEnum, TipoCursoEnum, SuscripcionCursoEnum
from src.schemas import CursoSchema, ExamenSchema, ColaboradorSchema, CursadaSchema, ExamenResueltoSchema
from src.services import curso_service, cursada_service

router = APIRouter(
    prefix="/cursos",
    tags=["cursos"]
)


@router.post("/", response_model=CursoSchema.CursoResponse)
def create_curso(curso: CursoSchema.CreateCursoRequest, db: Session = Depends(get_db)):
    return curso_service.crear_curso(curso=curso, db=db)


@router.get("/{curso_id}", response_model=CursoSchema.CursoResponse)
def get_curso(curso_id: uuid.UUID, db: Session = Depends(get_db)):
    return curso_service.get_curso(curso_id, db)


@router.delete("/{curso_id}", response_model=CursoSchema.CursoResponse)
def delete_curso(curso_id: uuid.UUID, db: Session = Depends(get_db)):
    return curso_service.eliminar_curso(curso_id, db)


@router.patch("/{curso_id}/bloquear", response_model=CursoSchema.CursoResponse)
def bloquear_curso(curso_id: uuid.UUID, db: Session = Depends(get_db)):
    return curso_service.bloquear_curso(curso_id, db)


@router.patch("/{curso_id}/activar", response_model=CursoSchema.CursoResponse)
def activar_curso(curso_id: uuid.UUID, db: Session = Depends(get_db)):
    return curso_service.activar_curso(curso_id, db)


@router.get("", response_model=List[CursoSchema.CursoResponse])
def get_cursos_by_estado(
        estados: Optional[List[EstadoCursoEnum]] = Query(None, alias="estado"),
        db: Session = Depends(get_db)):
    return curso_service.get_cursos(estados, db)


@router.get("/tipos/", response_model=List[CursoSchema.CursoResponse])
def get_cursos_by_tipo(
        tipos: Optional[List[TipoCursoEnum]] = Query(None, alias="tipo"),
        db: Session = Depends(get_db)):
    return curso_service.get_cursos_by_tipo_curso(tipos, db)


@router.get("/suscripciones/", response_model=List[CursoSchema.CursoResponse])
def get_cursos_by_suscripcion(
        suscripciones: Optional[List[SuscripcionCursoEnum]] = Query(None, alias="suscripcion"),
        db: Session = Depends(get_db)):
    return curso_service.get_cursos_by_suscripcion(suscripciones, db)


@router.put("/{curso_id}", response_model=CursoSchema.CursoResponse)
def editar_curso(curso_id: uuid.UUID, curso: CursoSchema.EditarCurso, db: Session = Depends(get_db)):
    return curso_service.editar_curso(curso_id=curso_id, curso=curso, db=db)


@router.post("/{curso_id}/inscribirse", response_model=CursadaSchema.CursadaResponse)
def inscribir_alumno(curso_id: uuid.UUID, user: CursadaSchema.InscribirAlumno, db: Session = Depends(get_db)):
    return cursada_service.inscribir_alumno(curso_id, user, db)


@router.put("/{curso_id}/desinscribirse", response_model=CursadaSchema.CursadaResponse)
def desinscribir_alumno(curso_id: uuid.UUID, user: CursadaSchema.InscribirAlumno, db: Session = Depends(get_db)):
    return cursada_service.desinscribir_alumno(curso_id, user, db)


@router.get("/{curso_id}/alumnos", response_model=List[str])
def get_listado_alumnos_curso(curso_id: uuid.UUID, db: Session = Depends(get_db)):
    return curso_service.get_listado_alumnos(curso_id, db)


@router.post("/colaborador", response_model=ColaboradorSchema.ColaboradorResponse)
def add_colaborador(colaborador: ColaboradorSchema.CreateColaboradorRequest, db: Session = Depends(get_db)):
    return curso_service.add_colaborador(colaborador, db)
