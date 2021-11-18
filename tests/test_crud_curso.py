from unittest import TestCase
from src.models.CursoModel import Curso


class CursoTest(TestCase):

    def testVerificarEstadoInicialCursoNuevo(self):
        curso = Curso(1, 'hola', 'descr', '#h1', 'idioma', '1', 'gratuito', 'virtual')
        self.assertTrue(curso.estado == 'activo')

    def testVerificarIdCreadorCursoNuevo(self):
        curso = Curso(1, 'hola', 'descr', '#h1', 'idioma', '1', 'gratuito', 'virtual')
        self.assertTrue(curso.id_creador == 1)

    def testVerificarTituloCursoNuevo(self):
        curso = Curso(1, 'hola', 'descr', '#h1', 'idioma', '1', 'gratuito', 'virtual')
        self.assertTrue(curso.titulo == 'hola')

    def testVerificarDescripcionCursoNuevo(self):
        curso = Curso(1, 'hola', 'descr', '#h1', 'idioma', '1', 'gratuito', 'virtual')
        self.assertTrue(curso.descripcion == 'descr')

    def testEliminarCursoVerificarEstado(self):
        curso = Curso(1, 'hola', 'descr', '#h1', 'idioma', '1', 'gratuito', 'virtual')
        curso.eliminar()
        self.assertTrue(curso.estado == 'eliminado')
