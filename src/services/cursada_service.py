import uuid
from typing import Optional, List

from src.db.repositories import cursada_repository, examen_resuelto_repository, examen_repository
from sqlalchemy.orm import Session
from fastapi import HTTPException

from src.models.CursadaModel import EstadoCursadaEnum
from src.models.ExamenModel import EstadoExamenEnum
from src.models.ExamenResueltoModel import EstadoExamenResueltoEnum, ExamenResuelto
from src.models.RespuestaModel import EstadoRespuestaEnum
from src.schemas import CursadaSchema, ExamenResueltoSchema


def inscribir_alumno(curso_id: uuid.UUID, user: CursadaSchema.InscribirAlumno, db: Session):
    # TODO: Validar que el username sea válido.
    return cursada_repository.inscribir_alumno(curso_id, user, db)


def get_cursada(curso_id: uuid.UUID, username: str, db: Session):
    db_cursada = cursada_repository.get_cursada(curso_id, username, db)
    if db_cursada is None:
        raise HTTPException(status_code=404, detail="Cursada not found")
    return db_cursada


def desinscribir_alumno(curso_id: uuid.UUID, user: CursadaSchema.InscribirAlumno, db: Session):
    db_cursada = get_cursada(curso_id, user.username, db)
    db_cursada.cambiar_estado_a_desinscripto()
    return cursada_repository.actualizar_cursada(db, db_cursada)


def add_examen_resuelto(examen_resuelto: ExamenResueltoSchema.CreateExamenResueltoRequest, db: Session):
    cursada = cursada_repository.get_cursada(examen_resuelto.id_curso, examen_resuelto.username, db)

    if cursada is None or cursada.estado != EstadoCursadaEnum.inscripto:
        raise HTTPException(status_code=400, detail="El usuario debe estar inscripto para poder rendir.")

    examen = examen_repository.get_examen(db, examen_resuelto.id_examen)

    if examen is None or examen.estado != EstadoExamenEnum.publicado:
        raise HTTPException(status_code=400, detail="El examen debe estar publicado para poder rendir.")

    examen_resuelto_db = \
        examen_resuelto_repository.create_examen_resuelto(db=db, examen_resuelto=examen_resuelto, id_cursada=cursada.id)

    cursada.actualizar()
    cursada_repository.actualizar_cursada(db, cursada)

    return examen_resuelto_db


def corregir_examen_resuelto(correccion: ExamenResueltoSchema.CorregirExamenRequest, db):
    examen_resuelto: ExamenResuelto = \
        examen_resuelto_repository.get_examen_resuelto_by_id(db, correccion.id_examen_resuelto)
    examen = examen_resuelto.examen

    corrector_es_creador = examen.curso.id_creador == correccion.corrector
    corrector_es_colaborador = False
    for colaborador in examen.curso.colaboradores:
        if colaborador.username == correccion.corrector:
            corrector_es_colaborador = True
            break

    if not corrector_es_creador and not corrector_es_colaborador:
        raise HTTPException(status_code=400, detail="El corrector debe ser creador o colaborador del curso.")

    if examen_resuelto is None:
        raise HTTPException(status_code=404, detail="Examen resuelto no encontrado.")

    if examen_resuelto.estado == EstadoExamenResueltoEnum.corregido:
        raise HTTPException(status_code=400, detail="El examen ya se encuentra corregido.")

    nota: int = 0

    for respuesta in examen_resuelto.respuestas:
        correccion_encontrada = False
        for correccion_respuesta in correccion.correcciones:
            if respuesta.id == correccion_respuesta.id_respuesta:
                correccion_encontrada = True
                if correccion_respuesta.es_correcta:
                    respuesta.estado = EstadoRespuestaEnum.correcta
                    nota += respuesta.consigna.puntaje
                else:
                    respuesta.estado = EstadoRespuestaEnum.incorrecta
                break

        if not correccion_encontrada:
            raise HTTPException(status_code=400, detail="No se corrigieron todas las respuestas.")

    examen_resuelto.nota = nota
    examen_resuelto.corrector = correccion.corrector
    examen_resuelto.estado = EstadoExamenResueltoEnum.corregido
    examen_resuelto.actualizar()
    examen_resuelto_repository.actualizar_examen_resuelto(db, examen_resuelto)

    return examen_resuelto

def get_historicos(username, db):
    db_cursada = cursada_repository.get_historicos(username, db)
    if len(db_cursada) == 0:
        raise HTTPException(status_code=404, detail="Cursada not found")
    return db_cursada
  
def get_examenes_resueltos_by_curso(
        curso_id: uuid.UUID,
        estados: Optional[List[EstadoExamenResueltoEnum]],
        db: Session):
    return examen_resuelto_repository.get_examenes_resueltos_by_curso(db, curso_id, estados)
