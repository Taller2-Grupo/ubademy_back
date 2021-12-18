from unittest import TestCase
from src.models.CursoModel import Curso
from fastapi import HTTPException
import pytest


class CursoTest(TestCase):

    def testEditarTitulo(self):
        curso = Curso(1, 'hola', 'descr', '#h1', 'idioma', 'gratuito')
        curso.set_titulo('titulo nuevo')

        self.assertTrue(curso.get_titulo() == 'titulo nuevo')

    def testEditarDescripcion(self):
        curso = Curso(1, 'hola', 'descr', '#h1', 'idioma', 'gratuito')
        curso.set_descripcion('descripcion nueva')

        self.assertTrue(curso.get_descripcion() == 'descripcion nueva')

    def testEditarEstadoValido(self):
        curso = Curso(1, 'hola', 'descr', '#h1', 'idioma', 'gratuito')
        curso.set_estado('bloqueado')

        self.assertTrue(curso.get_estado() == 'bloqueado')

    def testEditarEstadoInvalido(self):
        curso = Curso(1, 'hola', 'descr', '#h1', 'idioma', 'gratuito')

        with pytest.raises(HTTPException):
            curso.set_estado('inexistente')

    def testEditarHashtags(self):
        curso = Curso(1, 'hola', 'descr', '#h1', 'idioma', 'gratuito')
        curso.set_hashtags('#h1#h2')

        self.assertTrue(curso.get_hashtags() == '#h1#h2')

    def testEditarTipoValido(self):
        curso = Curso(1, 'hola', 'descr', '#h1', 'idioma', 'gratuito')
        curso.set_tipo('programacion')

        self.assertTrue(curso.get_tipo() == 'programacion')

    def testEditarTipoInvalido(self):
        curso = Curso(1, 'hola', 'descr', '#h1', 'idioma', 'gratuito')

        with pytest.raises(HTTPException):
            curso.set_tipo('inexistente')

    def testEditarSuscripcionValida(self):
        curso = Curso(1, 'hola', 'descr', '#h1', 'idioma', 'gratuito')
        curso.set_suscripcion('pago')

        self.assertTrue(curso.get_suscripcion() == 'pago')

    def testEditarSuscripcionInvalida(self):
        curso = Curso(1, 'hola', 'descr', '#h1', 'idioma', 'gratuito')

        with pytest.raises(HTTPException):
            curso.set_suscripcion('inexistente')
