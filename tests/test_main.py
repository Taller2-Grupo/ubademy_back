from unittest import TestCase
from fastapi.testclient import TestClient
from src.main import app
from sqlalchemy import create_engine, null
from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL = "postgresql://szbbimktemtmxp:abb783d6b84c1f607061d64dacb901af10cae40d24a2b6d96110d7efe477b5c4@ec2-54-174-172-218.compute-1.amazonaws.com:5432/d3vhnlg19iblmb"
#
# engine = create_engine(
#     SQLALCHEMY_DATABASE_URL
# )
# TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
#
#
# Base.metadata.create_all(bind=engine)
#
#
# def override_get_db():
#     try:
#         db = TestingSessionLocal()
#         yield db
#     finally:
#         db.close()
#
#
# app.dependency_overrides[get_db] = override_get_db
from src.models.CursoModel import EstadoCursoEnum

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
                               json={'id_creador': 'dadb4e2f-63d1-45d4-9f44-2d68a07105cc', 'titulo': 'postCurso'
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
                               json={'id_creador': 'dadb4e2f-63d1-45d4-9f44-2d68a07105cc', 'titulo': 'postCurso'
                                   , 'descripcion': 'descr', 'hashtags': 'hola', 'tipo': 'idioma', 'examenes': '1'
                                   , 'suscripcion':'sdfsdfs', 'ubicacion': 'virtual'})
        assert response.status_code == 400

    def testGetCursos(self):
        response = client.get('/cursos')
        assert response.status_code == 200

    def testGetCurso(self):
        response_post = client.post('/cursos/',
                    json={'id_creador': '615e3022-fd6a-4fd0-ba8b-0b8a3549a067', 'titulo': 'GetCurso'
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
                    json={'id_creador': 'fa3333cf-10e2-44df-9bc5-ae4c8d936c66', 'titulo': 'DeleteCurso'
                        , 'descripcion': 'descr', 'hashtags': 'hola', 'tipo': 'idioma', 'examenes': '1'
                        , 'suscripcion': 'gratuito', 'ubicacion': 'virtual'})
        id_post = response_post.json().get('id')
        response = client.delete('/cursos/' + id_post)
        assert response.status_code == 200

    def testEditarCurso(self):
        response_post = client.post('/cursos/',
                    json={'id_creador': 'fa3333cf-10e2-44df-9bc5-ae4c8d936c66', 'titulo': 'EditarTest'
                        , 'descripcion': 'descr', 'hashtags': 'hola', 'tipo': 'idioma', 'examenes': '1'
                        , 'suscripcion': 'gratuito', 'ubicacion': 'virtual'})
        id_post = response_post.json().get('id')
        response = client.put('/cursos/' + id_post, json={'nuevo_titulo': 'nuevoTitulo', 'nueva_descripcion': 'nuevaDescripcion'})
        self.assertTrue(response.json().get('titulo') == 'nuevoTitulo' and response.json().get('descripcion') == 'nuevaDescripcion')
        assert response.status_code == 200

    def testGetCursosCreadorSinCursos(self):
        response = client.get('4e4707da-0542-4f9c-ae59-bc3bcaafde71/cursos')
        assert response.status_code == 200

    def testGetCursosCreadorConCursos(self):
        client.post('/cursos/',
                    json={'id_creador': 'fa3333cf-10e2-44df-9bc5-ae4c8d936c66', 'titulo': 'CursosCreadorTest'
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




