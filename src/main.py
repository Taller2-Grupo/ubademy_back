import uuid
from typing import List

from fastapi import FastAPI, Depends
from src.routers import cursos_router, examen_router
from src.schemas import CursoSchema
from sqlalchemy.orm import Session
from src.db.database import get_db
from src.services import curso_service
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(cursos_router.router)
app.include_router(examen_router.router)


@app.get("/{creador_id}/cursos", response_model=List[CursoSchema.CursoResponse])
def get_cursos_creador(creador_id: uuid.UUID, db: Session = Depends(get_db)):
    return curso_service.get_cursos_creador(creador_id, db)


# Para debuguear:
# import uvicorn
# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8000)
