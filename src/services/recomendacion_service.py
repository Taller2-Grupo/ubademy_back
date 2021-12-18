import decimal
from collections import Counter

from fastapi import HTTPException
from sqlalchemy.orm import Session
from src.services import cursada_service
from src.db.repositories import cursada_repository


def recomendar_curso_por_intereses(db: Session, username: str):
    try:
        cursos = cursada_service.get_historicos(username, db)
    except HTTPException:
        return cursada_repository.get_cursos_mas_inscriptos(db)

    tipo_cursos = []
    ids_cursos = []

    for curso in cursos:
        tipo_cursos.append(curso.tipo)
        ids_cursos.append(str(curso.id))

    c = Counter(tipo_cursos)
    tipo_curso_favorito = c.most_common(1)[0][0]

    return cursada_repository.get_cursos_mas_inscriptos_by_tipo_curso(db, tipo_curso_favorito, ids_cursos)


def recomendar_cursos_por_ubicacion(db: Session, latitud: decimal.Decimal, longitud: decimal.Decimal):
    if latitud is None and longitud is None:
        return []

    return cursada_repository.get_cursos_by_cercania(db, latitud, longitud)
