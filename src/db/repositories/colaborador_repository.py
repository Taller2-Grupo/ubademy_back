from sqlalchemy.orm import Session

from src.models.ColaboradorModel import Colaborador
from src.schemas import ColaboradorSchema


def create_colaborador(db: Session, colaborador: ColaboradorSchema.CreateColaboradorRequest):
    db_colaborador = Colaborador(colaborador.id_curso, colaborador.username)
    db.add(db_colaborador)
    db.commit()
    db.refresh(db_colaborador)
    return db_colaborador
