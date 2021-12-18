from unittest import TestCase
from src.models.CursoModel import Curso
from fastapi import HTTPException


class CursoTest(TestCase):

    def testEditarTitulo(self):
        curso = Curso("test@test.com", 'hola', 'descr', '#h1', 'idioma', 'gratuito')
        curso.set_titulo('titulo nuevo')

        self.assertTrue(curso.get_titulo() == 'titulo nuevo')

    def testEditarDescripcion(self):
        curso = Curso("test@test.com", 'hola', 'descr', '#h1', 'idioma', 'gratuito')
        curso.set_descripcion('descripcion nueva')

        self.assertTrue(curso.get_descripcion() == 'descripcion nueva')

    def testEditarEstadoValido(self):
        curso = Curso("test@test.com", 'hola', 'descr', '#h1', 'idioma', 'gratuito')
        curso.set_estado('bloqueado')

        self.assertTrue(curso.get_estado() == 'bloqueado')

    def testEditarEstadoInvalido(self):
        curso = Curso("test@test.com", 'hola', 'descr', '#h1', 'idioma', 'gratuito')
        self.assertRaises(HTTPException, curso.set_estado, 'inexistente')

    def testEditarHashtags(self):
        curso = Curso("test@test.com", 'hola', 'descr', '#h1', 'idioma', 'gratuito')
        curso.set_hashtags('#h1#h2')

        self.assertTrue(curso.get_hashtags() == '#h1#h2')

    def testEditarTipoValido(self):
        curso = Curso("test@test.com", 'hola', 'descr', '#h1', 'idioma', 'gratuito')
        curso.set_tipo('programacion')

        self.assertTrue(curso.get_tipo() == 'programacion')

    def testEditarTipoInvalido(self):
        curso = Curso("test@test.com", 'hola', 'descr', '#h1', 'idioma', 'gratuito')
        self.assertRaises(HTTPException, curso.set_tipo, 'inexistente')

    def testEditarSuscripcionPremiumValida(self):
        curso = Curso("test@test.com", 'hola', 'descr', '#h1', 'idioma', 'gratuito')
        curso.set_suscripcion('premium')

        self.assertTrue(curso.get_suscripcion() == 'premium')

    def testEditarSuscripcionVipValida(self):
        curso = Curso("test@test.com", 'hola', 'descr', '#h1', 'idioma', 'gratuito')
        curso.set_suscripcion('vip')

        self.assertTrue(curso.get_suscripcion() == 'vip')

    def testEditarSuscripcionInvalida(self):
        curso = Curso("test@test.com", 'hola', 'descr', '#h1', 'idioma', 'gratuito')
        self.assertRaises(HTTPException, curso.set_suscripcion, 'inexistente')

    def testEditarLatitudLongitudNoNulos(self):
        curso = Curso("test@test.com", 'hola', 'descr', '#h1', 'idioma', 'gratuito')
        curso.set_latitud_and_longitud(10, 15)
        self.assertTrue(curso.latitud == 10)
        self.assertTrue(curso.longitud == 15)

    def testEditarLatitudLongitudNulos(self):
        curso = Curso("test@test.com", 'hola', 'descr', '#h1', 'idioma', 'gratuito')
        curso.set_latitud_and_longitud(None, None)
        self.assertTrue(curso.latitud is None)
        self.assertTrue(curso.longitud is None)

    def testEditarLatitudNoNulaLongitudNula(self):
        curso = Curso("test@test.com", 'hola', 'descr', '#h1', 'idioma', 'gratuito')
        self.assertRaises(HTTPException, curso.set_latitud_and_longitud, 10, None)

    def testEditarLatitudNulaLongitudNoNula(self):
        curso = Curso("test@test.com", 'hola', 'descr', '#h1', 'idioma', 'gratuito')
        self.assertRaises(HTTPException, curso.set_latitud_and_longitud, None, 15)
