from unittest import TestCase
from src.db.database import get_db, Base
from src.models.CursoModel import Curso
from src.schemas import CursoSchema
from src.schemas.CursoSchema import CreateCursoRequest
from src.services.curso_service import crear_curso

class CursoTest(TestCase):

    def testEditarTitulo(self):
        curso = Curso(1, 'hola', 'descr', '#h1', 'idioma', '1', 'gratuito', 'virtual')
        curso.cambiarTitulo('titulo nuevo')

        self.assertTrue(curso.titulo == 'titulo nuevo')

    def testEditarDescripcion(self):
        curso = Curso(1, 'hola', 'descr', '#h1', 'idioma', '1', 'gratuito', 'virtual')
        curso.cambiarDescripcion('descripcion nueva')

        self.assertTrue(curso.descripcion == 'descripcion nueva')