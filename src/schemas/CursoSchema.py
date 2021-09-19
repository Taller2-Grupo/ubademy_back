from fastapi import HTTPException
from pydantic import BaseModel, validator


class CursoBase(BaseModel):
    cantidad_alumnos: int
    cantidad_condicionales: int
    nombre: str

    @validator('cantidad_alumnos')
    def cantidad_menor_a_50(cls, cantidad):
        if cantidad > 50:
            raise HTTPException(status_code=400, detail='Bad Request')
        return cantidad


# En esta clase se le agregan todos los atributos particulares para la creación, en este caso ninguno.
class CursoCreate(CursoBase):
    pass


# Esto es lo que se va a devolver cuando se este "leyendo" un Curso, en este caso "id" que no se pasa al crear
class Curso(CursoBase):
    id: int

    class Config:
        orm_mode = True
