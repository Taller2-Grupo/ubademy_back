import fastapi
import uvicorn
from models import CursoModel

api = fastapi.FastAPI()


@api.get('/')
async def index():
    return {
        "message": "Hello World!",
        "status": "OK"
    }


@api.post('/curso')
def crear_curso(curso: CursoModel.CursoRequestModel):
    return curso

@api.get('/users')
def get_hardcoded_user():
    return {
        "user": "pedro123!",
        "password": "123456"
    }


uvicorn.run(api)
