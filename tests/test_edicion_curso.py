from unittest import TestCase
from src.db.database import get_db, Base
from src.models.CursoModel import Curso
from src.schemas import CursoSchema
from src.schemas.CursoSchema import CreateCursoRequest
from src.services.curso_service import crear_curso
from fastapi import HTTPException
import pytest


class CursoTest(TestCase):

    def testEditarTitulo(self):
        curso = Curso(1, 'hola', 'descr', '#h1', 'idioma', '1', 'gratuito', 'virtual')
        curso.set_titulo('titulo nuevo')

        self.assertTrue(curso.get_titulo() == 'titulo nuevo')

    def testEditarDescripcion(self):
        curso = Curso(1, 'hola', 'descr', '#h1', 'idioma', '1', 'gratuito', 'virtual')
        curso.set_descripcion('descripcion nueva')

        self.assertTrue(curso.get_descripcion() == 'descripcion nueva')

    def testEditarEstadoValido(self):
        curso = Curso(1, 'hola', 'descr', '#h1', 'idioma', '1', 'gratuito', 'virtual')
        curso.set_estado('bloqueado')

        self.assertTrue(curso.get_estado() == 'bloqueado')

    def testEditarEstadoInvalido(self):
        curso = Curso(1, 'hola', 'descr', '#h1', 'idioma', '1', 'gratuito', 'virtual')

        with pytest.raises(HTTPException):
            curso.set_estado('inexistente')

    def testEditarHashtags(self):
        curso = Curso(1, 'hola', 'descr', '#h1', 'idioma', '1', 'gratuito', 'virtual')
        curso.set_hashtags('#h1#h2')

        self.assertTrue(curso.get_hashtags() == '#h1#h2')

    def testEditarTipoValido(self):
        curso = Curso(1, 'hola', 'descr', '#h1', 'idioma', '1', 'gratuito', 'virtual')
        curso.set_tipo('programacion')

        self.assertTrue(curso.get_tipo() == 'programacion')

    def testEditarTipoInvalido(self):
        curso = Curso(1, 'hola', 'descr', '#h1', 'idioma', '1', 'gratuito', 'virtual')

        with pytest.raises(HTTPException):
            curso.set_tipo('inexistente')

    def testEditarExamenes(self):
        curso = Curso(1, 'hola', 'descr', '#h1', 'idioma', '1', 'gratuito', 'virtual')
        curso.set_examenes('2')

        self.assertTrue(curso.get_examenes() == '2')

    def testEditarSuscripcionValida(self):
        curso = Curso(1, 'hola', 'descr', '#h1', 'idioma', '1', 'gratuito', 'virtual')
        curso.set_suscripcion('pago')

        self.assertTrue(curso.get_suscripcion() == 'pago')

    def testEditarSuscripcionInvalida(self):
        curso = Curso(1, 'hola', 'descr', '#h1', 'idioma', '1', 'gratuito', 'virtual')

        with pytest.raises(HTTPException):
            curso.set_suscripcion('inexistente')

    def testEditarUbicacion(self):
        curso = Curso(1, 'hola', 'descr', '#h1', 'idioma', '1', 'gratuito', 'virtual')
        curso.set_ubicacion('paseo colon')

        self.assertTrue(curso.get_ubicacion() == 'paseo colon')