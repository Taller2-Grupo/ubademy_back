import uuid
from typing import Optional
from pydantic import BaseModel, validator
from fastapi import HTTPException


class FavoritoBase(BaseModel):
    username: Optional[str]
    curso_id: Optional[str]


class FavearCurso(FavoritoBase):
    @validator('username')
    def tiene_username(cls, username: str):
        if not username:
            raise HTTPException(status_code=400, detail='Debe proporcionar un nombre de usuario.')
        return username

    @validator('curso_id')
    def tiene_curso_id(cls, curso_id: str):
        if not curso_id:
            raise HTTPException(status_code=400, detail='Debe proporcionar el id del curso.')
        return curso_id


# Esto es lo que se va a devolver cuando se este "leyendo" un Colaborador
class FavoritoResponse(FavoritoBase):
    class Config:
        orm_mode = True


class EsFavoritoResponse(FavoritoBase):
    value: bool

    class Config:
        orm_mode = True
