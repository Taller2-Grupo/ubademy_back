from fastapi import HTTPException
from pydantic import BaseModel, validator


class CursoRequestModel(BaseModel):
    cantidad_alumnos: int
    condicionales: int

    @validator('cantidad_alumnos')
    def cantidad_menor_a_50(cls, cantidad):
        if cantidad > 50:
            raise HTTPException(status_code=400, detail='Bad Request')
        return cantidad
