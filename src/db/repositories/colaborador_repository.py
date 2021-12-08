from fastapi import HTTPException
from sqlalchemy.orm import Session

from src.models.ColaboradorModel import Colaborador
from src.schemas import ColaboradorSchema
from src.schemas.ColaboradorSchema import DeleteColaboradorRequest


def create_colaborador(db: Session, colaborador: ColaboradorSchema.CreateColaboradorRequest):
    db_colaborador = Colaborador(colaborador.id_curso, colaborador.username)
    db.add(db_colaborador)
    db.commit()
    db.refresh(db_colaborador)
    return db_colaborador


def delete_colaborador(db: Session, colaborador: DeleteColaboradorRequest):
    db_colaborador = \
        db.query(Colaborador).filter(
            Colaborador.username == colaborador.username,
            Colaborador.id_curso == colaborador.id_curso
        ).first()

    if db_colaborador is None:
        raise HTTPException(status_code=404, detail="No existe el colaborador")

    db.delete(db_colaborador)
    db.commit()