from unittest import TestCase

from fastapi import HTTPException

from src.models.CursoModel import Curso


class CursoTest(TestCase):

    def testCursoNuevo(self):
        curso = Curso('test@test.com', 'hola', 'descr', '#h1', 'idioma', 'gratuito')
        self.assertTrue(curso.id_creador == 'test@test.com')
        self.assertTrue(curso.titulo == 'hola')
        self.assertTrue(curso.descripcion == 'descr')
        self.assertTrue(curso.estado == 'activo')
        self.assertTrue(curso.tipo == 'idioma')
        self.assertTrue(curso.suscripcion == 'gratuito')
        self.assertTrue(curso.latitud is None)
        self.assertTrue(curso.longitud is None)

    def testCursoNuevoConUbicacion(self):
        curso = Curso('test@test.com', 'hola', 'descr', '#h1', 'idioma', 'gratuito', 10, 15)
        self.assertTrue(curso.id_creador == 'test@test.com')
        self.assertTrue(curso.titulo == 'hola')
        self.assertTrue(curso.descripcion == 'descr')
        self.assertTrue(curso.estado == 'activo')
        self.assertTrue(curso.tipo == 'idioma')
        self.assertTrue(curso.suscripcion == 'gratuito')
        self.assertTrue(curso.latitud == 10)
        self.assertTrue(curso.longitud == 15)

    def testCursoNuevoSinLongitud(self):
        self.assertRaises(HTTPException, Curso, 'test@test.com', 'hola', 'descr', '#h1', 'idioma', 'gratuito', 10)

    def testCursoNuevoSinLatitud(self):
        self.assertRaises(HTTPException, Curso, 'test@test.com', 'hola', 'descr', '#h1', 'idioma', 'gratuito', None, 10)

    def testEliminarCursoVerificarEstado(self):
        curso = Curso('test@test.com', 'hola', 'descr', '#h1', 'idioma', 'gratuito')
        curso.eliminar()
        self.assertTrue(curso.estado == 'eliminado')
