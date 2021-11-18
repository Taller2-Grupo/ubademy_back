from unittest import TestCase
from fastapi.testclient import TestClient
from src.main import app
from src.models.CursadaModel import EstadoCursadaEnum

client = TestClient(app)


class MainTest(TestCase):

    def testPostCurso(self):
        response = client.post('/cursos/',
                               json={'id_creador': 'Renzo', 'titulo': 'postCurso'
                                   , 'descripcion': 'descr', 'hashtags': 'hola', 'tipo': 'idioma', 'examenes': '1'
                                   , 'suscripcion':'gratuito', 'ubicacion': 'virtual'})
        assert response.status_code == 200

    def testPostCursoSinTitulo(self):
        response = client.post('/cursos/',
                               json={'id_creador': 'Renzo'
                                   , 'descripcion': 'descr', 'hashtags': 'hola', 'tipo': 'idioma', 'examenes': '1'
                                   , 'suscripcion':'gratuito', 'ubicacion': 'virtual'})
        assert response.status_code == 400

    def testPostCursoSinDescripcion(self):
        response = client.post('/cursos/',
                               json={'id_creador': 'Renzo', 'titulo': 'postCurso'
                                   , 'hashtags': 'hola', 'tipo': 'idioma', 'examenes': '1'
                                   , 'suscripcion':'gratuito', 'ubicacion': 'virtual'})
        assert response.status_code == 400

    def testPostCursoSinTipo(self):
        response = client.post('/cursos/',
                               json={'id_creador': 'Renzo', 'titulo': 'postCurso'
                                   , 'descripcion': 'descr', 'hashtags': 'hola', 'examenes': '1'
                                   , 'suscripcion':'gratuito', 'ubicacion': 'virtual'})
        assert response.status_code == 400

    def testPostCursoTipoErroneo(self):
        response = client.post('/cursos/',
                               json={'id_creador': 'Renzo', 'titulo': 'postCurso'
                                   , 'descripcion': 'descr', 'hashtags': 'hola', 'tipo': 'dsfsdfsd', 'examenes': '1'
                                   , 'suscripcion':'gratuito', 'ubicacion': 'virtual'})
        assert response.status_code == 400

    def testPostCursoSinSuscripcion(self):
        response = client.post('/cursos/',
                               json={'id_creador': 'Renzo', 'titulo': 'postCurso'
                                   , 'descripcion': 'descr', 'hashtags': 'hola', 'tipo': 'idioma', 'examenes': '1'
                                   , 'ubicacion': 'virtual'})
        assert response.status_code == 400

    def testPostCursoSuscripcionErronea(self):
        response = client.post('/cursos/',
                               json={'id_creador': 'Renzo', 'titulo': 'postCurso'
                                   , 'descripcion': 'descr', 'hashtags': 'hola', 'tipo': 'idioma', 'examenes': '1'
                                   , 'suscripcion':'sdfsdfs', 'ubicacion': 'virtual'})
        assert response.status_code == 400

    def testGetCursos(self):
        response = client.get('/cursos')
        assert response.status_code == 200

    def testGetCurso(self):
        response_post = client.post('/cursos/',
                    json={'id_creador': 'Renzo', 'titulo': 'GetCurso'
                        , 'descripcion': 'descr', 'hashtags': 'hola', 'tipo': 'idioma', 'examenes': '1'
                        , 'suscripcion': 'gratuito', 'ubicacion': 'virtual'})
        id_post = response_post.json().get('id')
        response = client.get('/cursos/' + id_post)
        assert response.status_code == 200

    def testGetCursoInexistente(self):
        response = client.get('/cursos/58738aa9-a3ee-4ca9-8b36-4a0c20c1693f')
        assert response.status_code == 404

    def testDeleteCurso(self):
        response_post = client.post('/cursos/',
                    json={'id_creador': 'Renzo', 'titulo': 'DeleteCurso'
                        , 'descripcion': 'descr', 'hashtags': 'hola', 'tipo': 'idioma', 'examenes': '1'
                        , 'suscripcion': 'gratuito', 'ubicacion': 'virtual'})
        id_post = response_post.json().get('id')
        response = client.delete('/cursos/' + id_post)
        assert response.status_code == 200

    def testEditarTituloCurso(self):
        response_post = client.post('/cursos/',
                    json={'id_creador': 'Renzo', 'titulo': 'EditarTest'
                        , 'descripcion': 'descr', 'hashtags': 'hola', 'tipo': 'idioma', 'examenes': '1'
                        , 'suscripcion': 'gratuito', 'ubicacion': 'virtual'})
        id_post = response_post.json().get('id')
        response = client.put('/cursos/' + id_post, json={'nuevo_titulo': 'nuevoTitulo'})
        self.assertTrue(response.json().get('titulo') == 'nuevoTitulo' and response.status_code == 200)

    def testEditarDescripcionCurso(self):
        response_post = client.post('/cursos/',
                    json={'id_creador': 'Renzo', 'titulo': 'EditarTest'
                        , 'descripcion': 'descr', 'hashtags': 'hola', 'tipo': 'idioma', 'examenes': '1'
                        , 'suscripcion': 'gratuito', 'ubicacion': 'virtual'})
        id_post = response_post.json().get('id')
        response = client.put('/cursos/' + id_post, json={'nueva_descripcion': 'nuevaDescripcion'})
        self.assertTrue(response.json().get('descripcion') == 'nuevaDescripcion' and response.status_code == 200)

    def testEditarEstadoValidoCurso(self):
        response_post = client.post('/cursos/',
                    json={'id_creador': 'Renzo', 'titulo': 'EditarTest'
                        , 'descripcion': 'descr', 'hashtags': 'hola', 'tipo': 'idioma', 'examenes': '1'
                        , 'suscripcion': 'gratuito', 'ubicacion': 'virtual'})
        id_post = response_post.json().get('id')
        response = client.put('/cursos/' + id_post, json={'nuevo_estado': 'bloqueado'})
        self.assertTrue(response.json().get('estado') == 'bloqueado' and response.status_code == 200)

    def testEditarEstadoInvalidoCurso(self):
        response_post = client.post('/cursos/',
                    json={'id_creador': 'Renzo', 'titulo': 'EditarTest'
                        , 'descripcion': 'descr', 'hashtags': 'hola', 'tipo': 'idioma', 'examenes': '1'
                        , 'suscripcion': 'gratuito', 'ubicacion': 'virtual'})
        id_post = response_post.json().get('id')
        response = client.put('/cursos/' + id_post, json={'nuevo_estado': 'inexistente'})
        assert response.status_code == 400

    def testEditarHashtagsCurso(self):
        response_post = client.post('/cursos/',
                    json={'id_creador': 'Renzo', 'titulo': 'EditarTest'
                        , 'descripcion': 'descr', 'hashtags': 'hola', 'tipo': 'idioma', 'examenes': '1'
                        , 'suscripcion': 'gratuito', 'ubicacion': 'virtual'})
        id_post = response_post.json().get('id')
        response = client.put('/cursos/' + id_post, json={'nuevos_hashtags': '#h1'})
        self.assertTrue(response.json().get('hashtags') == '#h1' and response.status_code == 200)

    def testEditarTipoValidoCurso(self):
        response_post = client.post('/cursos/',
                    json={'id_creador': 'Renzo', 'titulo': 'EditarTest'
                        , 'descripcion': 'descr', 'hashtags': 'hola', 'tipo': 'idioma', 'examenes': '1'
                        , 'suscripcion': 'gratuito', 'ubicacion': 'virtual'})
        id_post = response_post.json().get('id')
        response = client.put('/cursos/' + id_post, json={'nuevo_tipo': 'programacion'})
        self.assertTrue(response.json().get('tipo') == 'programacion' and response.status_code == 200)

    def testEditarTipoInvalidoCurso(self):
        response_post = client.post('/cursos/',
                    json={'id_creador': 'Renzo', 'titulo': 'EditarTest'
                        , 'descripcion': 'descr', 'hashtags': 'hola', 'tipo': 'idioma', 'examenes': '1'
                        , 'suscripcion': 'gratuito', 'ubicacion': 'virtual'})
        id_post = response_post.json().get('id')
        response = client.put('/cursos/' + id_post, json={'nuevo_tipo': 'inexistente'})
        assert response.status_code == 400

    def testEditarExamenesCurso(self):
        response_post = client.post('/cursos/',
                    json={'id_creador': 'Renzo', 'titulo': 'EditarTest'
                        , 'descripcion': 'descr', 'hashtags': 'hola', 'tipo': 'idioma', 'examenes': '1'
                        , 'suscripcion': 'gratuito', 'ubicacion': 'virtual'})
        id_post = response_post.json().get('id')
        response = client.put('/cursos/' + id_post, json={'nuevos_examenes': '2'})
        self.assertTrue(response.json().get('examenes') == '2' and response.status_code == 200)

    def testEditarSuscripcionValidaCurso(self):
        response_post = client.post('/cursos/',
                    json={'id_creador': 'Renzo', 'titulo': 'EditarTest'
                        , 'descripcion': 'descr', 'hashtags': 'hola', 'tipo': 'idioma', 'examenes': '1'
                        , 'suscripcion': 'gratuito', 'ubicacion': 'virtual'})
        id_post = response_post.json().get('id')
        response = client.put('/cursos/' + id_post, json={'nueva_suscripcion': 'pago'})
        self.assertTrue(response.json().get('suscripcion') == 'pago' and response.status_code == 200)

    def testEditarSuscripcionInvalidaCurso(self):
        response_post = client.post('/cursos/',
                    json={'id_creador': 'Renzo', 'titulo': 'EditarTest'
                        , 'descripcion': 'descr', 'hashtags': 'hola', 'tipo': 'idioma', 'examenes': '1'
                        , 'suscripcion': 'gratuito', 'ubicacion': 'virtual'})
        id_post = response_post.json().get('id')
        response = client.put('/cursos/' + id_post, json={'nueva_suscripcion': 'inexistente'})
        assert response.status_code == 400

    def testEditarUbicacionCurso(self):
        response_post = client.post('/cursos/',
                    json={'id_creador': 'Renzo', 'titulo': 'EditarTest'
                        , 'descripcion': 'descr', 'hashtags': 'hola', 'tipo': 'idioma', 'examenes': '1'
                        , 'suscripcion': 'gratuito', 'ubicacion': 'virtual'})
        id_post = response_post.json().get('id')
        response = client.put('/cursos/' + id_post, json={'nueva_ubicacion': 'paseo colon'})
        self.assertTrue(response.json().get('ubicacion') == 'paseo colon' and response.status_code == 200)

    def testGetCursosCreadorSinCursos(self):
        response = client.get('4e4707da-0542-4f9c-ae59-bc3bcaafde71/cursos')
        assert response.status_code == 200

    def testGetCursosCreadorConCursos(self):
        client.post('/cursos/',
                    json={'id_creador': 'Renzo', 'titulo': 'CursosCreadorTest'
                        , 'descripcion': 'descr', 'hashtags': 'hola', 'tipo': 'idioma', 'examenes': '1'
                        , 'suscripcion': 'gratuito', 'ubicacion': 'virtual'})
        response = client.get('fa3333cf-10e2-44df-9bc5-ae4c8d936c66/cursos')
        assert response.status_code == 200

    def testInscribirseCurso(self):
        response_post = client.post('/cursos/',
                                    json={'id_creador': 'hola@gmail.com', 'titulo': 'InscribirseTest'
                                        , 'descripcion': 'descr', 'hashtags': 'hola', 'tipo': 'idioma', 'examenes': '1'
                                        , 'suscripcion': 'gratuito', 'ubicacion': 'virtual'})
        id_post = response_post.json().get('id')
        response = client.post('/cursos/' + id_post + '/inscribirse', json={'username': 'admin@admin.com'})
        assert response.status_code == 200

    def testInscribirseCursoSinUsername(self):
        response_post = client.post('/cursos/',
                                    json={'id_creador': 'hola@gmail.com', 'titulo': 'InscribirseTest'
                                        , 'descripcion': 'descr', 'hashtags': 'hola', 'tipo': 'idioma', 'examenes': '1'
                                        , 'suscripcion': 'gratuito', 'ubicacion': 'virtual'})
        id_post = response_post.json().get('id')
        response = client.post('/cursos/' + id_post + '/inscribirse', json={})
        assert response.status_code == 400

    def testInscribirseCursoDosVeces(self):
        response_post = client.post('/cursos/',
                                    json={'id_creador': 'hola@gmail.com', 'titulo': 'InscribirseTest'
                                        , 'descripcion': 'descr', 'hashtags': 'hola', 'tipo': 'idioma', 'examenes': '1'
                                        , 'suscripcion': 'gratuito', 'ubicacion': 'virtual'})
        id_post = response_post.json().get('id')
        client.post('/cursos/' + id_post + '/inscribirse', json={'username': 'admin@admin.com'})
        response = client.post('/cursos/' + id_post + '/inscribirse', json={'username': 'admin@admin.com'})
        assert response.status_code == 400

    def testDesinscribirseCurso(self):
        response_post = client.post('/cursos/',
                                    json={'id_creador': 'hola@gmail.com', 'titulo': 'DesinscribirseTest'
                                        , 'descripcion': 'descr', 'hashtags': 'hola', 'tipo': 'idioma', 'examenes': '1'
                                        , 'suscripcion': 'gratuito', 'ubicacion': 'virtual'})
        id_post = response_post.json().get('id')
        client.post('/cursos/' + id_post + '/inscribirse', json={'username': 'admin@admin.com'})
        response = client.put('/cursos/' + id_post + '/desinscribirse', json={'username': 'admin@admin.com'})
        assert response.json().get('estado') == EstadoCursadaEnum.desinscripto
        assert response.status_code == 200

    def testDesinscribirseCursoInexistente(self):
        response_post = client.post('/cursos/',
                                    json={'id_creador': 'hola@gmail.com', 'titulo': 'DesinscribirseTest'
                                        , 'descripcion': 'descr', 'hashtags': 'hola', 'tipo': 'idioma', 'examenes': '1'
                                        , 'suscripcion': 'gratuito', 'ubicacion': 'virtual'})
        id_post = response_post.json().get('id')
        client.post('/cursos/' + id_post + '/inscribirse', json={'username': 'admin@admin.com'})
        response = client.put('/cursos/4311b8ad-9178-403d-9d9b-d9070378b95f/desinscribirse', json={'username': 'admin@admin.com'})
        assert response.status_code == 404

    def testGetListadoDeAlumnosCursoExistente(self):
        response_post = client.post('/cursos/',
                                    json={'id_creador': 'hola@gmail.com', 'titulo': 'ListadoTest'
                                        , 'descripcion': 'descr', 'hashtags': 'hola', 'tipo': 'idioma', 'examenes': '1'
                                        , 'suscripcion': 'gratuito', 'ubicacion': 'virtual'})
        id_post = response_post.json().get('id')
        client.post('/cursos/' + id_post + '/inscribirse', json={'username': 'admin@admin.com'})
        client.post('/cursos/' + id_post + '/inscribirse', json={'username': 'admin2@admin.com'})
        client.post('/cursos/' + id_post + '/inscribirse', json={'username': 'admin3@admin.com'})
        response = client.get('/cursos/' + id_post + '/alumnos')
        self.assertTrue(response.status_code == 200 and response.json() == ['admin@admin.com', 'admin2@admin.com', 'admin3@admin.com'])

    def testGetListadoDeAlumnosCursoInexistente(self):
        response = client.get('/cursos/c8886379-356d-49f7-8fc2-d6a566a8384d/alumnos')
        assert response.status_code == 404

    def testGetListadoDeAlumnosCursoExistenteAlumnoDesinscripto(self):
        response_post = client.post('/cursos/',
                                    json={'id_creador': 'holaa@gmail.com', 'titulo': 'ListadoDesinscriptoTest'
                                        , 'descripcion': 'descr', 'hashtags': 'hola', 'tipo': 'idioma', 'examenes': '1'
                                        , 'suscripcion': 'gratuito', 'ubicacion': 'virtual'})
        id_post = response_post.json().get('id')
        client.post('/cursos/' + id_post + '/inscribirse', json={'username': 'admin11@admin.com'})
        client.post('/cursos/' + id_post + '/inscribirse', json={'username': 'admin12@admin.com'})
        client.post('/cursos/' + id_post + '/inscribirse', json={'username': 'admin13@admin.com'})
        client.put('/cursos/' + id_post + '/desinscribirse', json={'username': 'admin13@admin.com'})

        response = client.get('/cursos/' + id_post + '/alumnos')

        self.assertTrue(response.status_code == 200 and response.json() == ['admin11@admin.com', 'admin12@admin.com'])

    def testGetListadoDeAlumnosCursoExistenteAlumnoInscriptoDespuesDeDesinscripto(self):
        response_post = client.post('/cursos/',
                                    json={'id_creador': 'holaa@gmail.com', 'titulo': 'ListadoInscriptoDesinscriptoInscriptoTest'
                                        , 'descripcion': 'descr', 'hashtags': 'hola', 'tipo': 'idioma', 'examenes': '1'
                                        , 'suscripcion': 'gratuito', 'ubicacion': 'virtual'})
        id_post = response_post.json().get('id')
        client.post('/cursos/' + id_post + '/inscribirse', json={'username': 'admin111@admin.com'})
        client.put('/cursos/' + id_post + '/desinscribirse', json={'username': 'admin111@admin.com'})
        client.post('/cursos/' + id_post + '/inscribirse', json={'username': 'admin111@admin.com'})

        response = client.get('/cursos/' + id_post + '/alumnos')

        self.assertTrue(response.status_code == 200 and response.json() == ['admin111@admin.com'])

    def test_get_curso_by_tipo(self):
        response = client.get('/cursos/tipos/?tipo=idioma')
        assert response.status_code == 200

    def test_get_curso_by_suscripcion(self):
        response = client.get('/cursos/suscripciones/?suscripcion=gratuito')
        assert response.status_code == 200

    def test_agregar_colaborador(self):
        response_post = client.post('/cursos/',
                                    json={'id_creador': 'hola@gmail.com', 'titulo': 'InscribirseTest',
                                          'descripcion': 'descr', 'hashtags': 'hola', 'tipo': 'idioma', 'examenes': '1',
                                          'suscripcion': 'gratuito', 'ubicacion': 'virtual'})
        id_post = response_post.json().get('id')
        response = client.post('/cursos/colaborador', json={'username': 'admin@admin.com', 'id_curso': id_post})
        assert response.status_code == 200

    def test_agregar_colaborador_dos_veces(self):
        response_post = client.post('/cursos/',
                                    json={'id_creador': 'hola@gmail.com', 'titulo': 'InscribirseTest',
                                          'descripcion': 'descr', 'hashtags': 'hola', 'tipo': 'idioma', 'examenes': '1',
                                          'suscripcion': 'gratuito', 'ubicacion': 'virtual'})
        id_post = response_post.json().get('id')
        response_1 = client.post('/cursos/colaborador', json={'username': 'admin@admin.com', 'id_curso': id_post})
        response_2 = client.post('/cursos/colaborador', json={'username': 'admin@admin.com', 'id_curso': id_post})
        assert response_1.status_code == 200
        assert response_2.status_code == 422






