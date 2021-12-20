import decimal
from collections import Counter

from fastapi import HTTPException
from sqlalchemy.orm import Session
from src.services import cursada_service
from src.db.repositories import cursada_repository, curso_repository


def recomendar_curso_por_intereses(db: Session, username: str):
    try:
        cursos = cursada_service.get_historicos(username, db)
    except HTTPException:
        cursos_id = cursada_repository.get_cursos_mas_inscriptos(db)
        return curso_repository.get_cursos(cursos_id, db)

    tipo_cursos = []
    ids_cursos = []

    for curso in cursos:
        tipo_cursos.append(curso.tipo)
        ids_cursos.append(str(curso.id))

    c = Counter(tipo_cursos)
    tipo_curso_favorito = c.most_common(1)[0][0]

    cursos_id = cursada_repository.get_cursos_mas_inscriptos_by_tipo_curso(db, tipo_curso_favorito, ids_cursos)
    return curso_repository.get_cursos(cursos_id, db)


def recomendar_cursos_por_ubicacion(db: Session, latitud: decimal.Decimal, longitud: decimal.Decimal):
    if latitud is None and longitud is None:
        return []

    return cursada_repository.get_cursos_by_cercania(db, latitud, longitud)
