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

        self.assertTrue(curso.getTitulo() == 'titulo nuevo')

    def testEditarDescripcion(self):
        curso = Curso(1, 'hola', 'descr', '#h1', 'idioma', '1', 'gratuito', 'virtual')
        curso.cambiarDescripcion('descripcion nueva')

        self.assertTrue(curso.getDescripcion() == 'descripcion nueva')

    def testEditarHashtags(self):
        curso = Curso(1, 'hola', 'descr', '#h1', 'idioma', '1', 'gratuito', 'virtual')
        curso.cambiarHashtags('#h1#h2')

        self.assertTrue(curso.getHashtags() == '#h1#h2')

    def testEditarExamenes(self):
        curso = Curso(1, 'hola', 'descr', '#h1', 'idioma', '1', 'gratuito', 'virtual')
        curso.cambiarExamenes('2')

        self.assertTrue(curso.getExamenes() == '2')

    def testEditarUbicacion(self):
        curso = Curso(1, 'hola', 'descr', '#h1', 'idioma', '1', 'gratuito', 'virtual')
        curso.cambiarUbicacion('paseo colon')

        self.assertTrue(curso.getUbicacion() == 'paseo colon')