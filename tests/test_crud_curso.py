from unittest import TestCase
from src.db.database import get_db, Base
from src.models.CursoModel import Curso
from src.schemas import CursoSchema
from src.schemas.CursoSchema import CreateCursoRequest
from src.services.curso_service import crear_curso

class CursoTest(TestCase):

    def testVerificarEstadoInicialCursoNuevo(self):
        curso = Curso(1, 'hola', 'descr')
        self.assertTrue(curso.estado == 'activo')

    def testVerificarIdCreadorCursoNuevo(self):
        curso = Curso(1, 'hola', 'descr')
        self.assertTrue(curso.id_creador == 1)

    def testVerificarTituloCursoNuevo(self):
        curso = Curso(1, 'hola', 'descr')
        self.assertTrue(curso.titulo == 'hola')

    def testVerificarDescripcionCursoNuevo(self):
        curso = Curso(1, 'hola', 'descr')
        self.assertTrue(curso.descripcion == 'descr')

    def testEliminarCursoVerificarEstado(self):
        curso = Curso(1, 'hola', 'descr')
        curso.eliminar()
        self.assertTrue(curso.estado == 'eliminado')



