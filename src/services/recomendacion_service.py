from collections import Counter

from sqlalchemy.orm import Session
from src.services import cursada_service
from src.db.repositories import cursada_repository


def recomendar_curso_por_intereses(db: Session, username: str):
    cursos = cursada_service.get_historicos(username, db)
    tipo_cursos = []
    ids_cursos = []

    for curso in cursos:
        tipo_cursos.append(curso.tipo)
        ids_cursos.append(str(curso.id))

    c = Counter(tipo_cursos)
    tipo_curso_favorito = c.most_common(1)[0][0]

    return cursada_repository.get_cursos_mas_inscriptos(db, tipo_curso_favorito, ids_cursos)
