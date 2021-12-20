import uuid

from sqlalchemy.orm import Session

from src.models.ColaboradorModel import Colaborador
from src.models.CursadaModel import Cursada, EstadoCursadaEnum
from src.models.CursoModel import Curso, EstadoCursoEnum, TipoCursoEnum, SuscripcionCursoEnum
from src.models.FavoritoModel import Favorito
from src.schemas import CursoSchema
from typing import List, Optional


def get_curso(db: Session, curso_id: uuid.UUID):
    return db.query(Curso).filter(Curso.id == curso_id).first()


def get_cursos_creador(db: Session, creador: str):
    cursos = []
    for curso in db.query(Curso):
        if curso.id_creador == creador:
            cursos.append(curso)
    return cursos


def create_curso(db: Session, curso: CursoSchema.CreateCursoRequest):
    curso.tiene_titulo(curso.titulo)
    curso.tiene_descripcion(curso.descripcion)
    curso.tiene_tipo(curso.tipo)
    curso.tiene_suscripcion(curso.suscripcion)
    db_curso = Curso(
        curso.id_creador,
        curso.titulo,
        curso.descripcion,
        curso.hashtags,
        curso.tipo,
        curso.suscripcion,
        curso.latitud,
        curso.longitud
    )
    db.add(db_curso)
    db.commit()
    db.refresh(db_curso)
    return db_curso


def actualizar_curso(db: Session, curso: Curso):
    db.add(curso)
    db.commit()
    db.refresh(curso)
    return curso


def get_curso_by_estados(estados: Optional[List[EstadoCursoEnum]], db: Session):
    if estados is None:
        return db.query(Curso).all()
    return db.query(Curso).filter(Curso.estado.in_(estados)).all()


def get_curso_by_tipo_curso(tipos: Optional[List[TipoCursoEnum]], db: Session):
    if tipos is None:
        return db.query(Curso).all()
    return db.query(Curso).filter(Curso.tipo.in_(tipos)).all()


def get_curso_by_suscripcion(suscripciones: Optional[List[SuscripcionCursoEnum]], db: Session):
    if suscripciones is None:
        return db.query(Curso).all()
    return db.query(Curso).filter(Curso.suscripcion.in_(suscripciones)).all()


def get_listado_alumnos(curso_id: uuid.UUID, db: Session):
    cursadas = db.query(Cursada).filter(Cursada.curso_id == curso_id,
                                        Cursada.estado == EstadoCursadaEnum.inscripto).all()
    listado = []
    for cursada in cursadas:
        listado.append(cursada.username)
    return listado


def add_favorito(favorito, db):
    username = favorito.tiene_username(favorito.username)
    curso_id = favorito.tiene_curso_id(favorito.curso_id)
    db_favorito = Favorito(username, curso_id)
    db.add(db_favorito)
    db.commit()
    db.refresh(db_favorito)
    return db_favorito


def get_favoritos(username, db):
    id_cursos = db.query(Favorito).filter(Favorito.username == username).with_entities(Favorito.curso_id).all()
    id_cursos_string = []
    for curso_id in id_cursos:
        id_cursos_string.append(str(curso_id)[2:38])
    return db.query(Curso).filter(Curso.id.in_(id_cursos_string)).all()


def get_cursos_colaborador(db, username):
    id_cursos = db.query(Colaborador).filter(Colaborador.username == username).with_entities(
        Colaborador.id_curso).all()
    id_cursos_string = []
    for curso_id in id_cursos:
        id_cursos_string.append(str(curso_id)[7:43])
    return db.query(Curso).filter(Curso.id.in_(id_cursos_string)).all()
