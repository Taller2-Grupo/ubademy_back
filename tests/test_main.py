from fastapi.testclient import TestClient
from src.main import app
from src.models.CursadaModel import EstadoCursadaEnum
from src.models.ExamenModel import EstadoExamenEnum
from src.models.ExamenResueltoModel import EstadoExamenResueltoEnum

client = TestClient(app)


def test_post_curso():
    response = client.post('/cursos/',
                           json={'id_creador': 'Renzo', 'titulo': 'postCurso',
                                 'descripcion': 'descr', 'hashtags': 'hola', 'tipo': 'idioma',
                                 'suscripcion': 'gratuito', 'ubicacion': 'virtual'})
    assert response.status_code == 200


def test_post_curso_sin_titulo():
    response = client.post('/cursos/',
                           json={'id_creador': 'Renzo', 'descripcion': 'descr', 'hashtags': 'hola',
                                 'tipo': 'idioma', 'suscripcion': 'gratuito', 'ubicacion': 'virtual'})
    assert response.status_code == 400


def test_post_curso_sin_descripcion():
    response = client.post('/cursos/',
                           json={'id_creador': 'Renzo', 'titulo': 'postCurso',
                                 'hashtags': 'hola', 'tipo': 'idioma',
                                 'suscripcion': 'gratuito', 'ubicacion': 'virtual'})
    assert response.status_code == 400


def test_post_curso_sin_tipo():
    response = client.post('/cursos/',
                           json={'id_creador': 'Renzo', 'titulo': 'postCurso',
                                 'descripcion': 'descr', 'hashtags': 'hola',
                                 'suscripcion': 'gratuito', 'ubicacion': 'virtual'})
    assert response.status_code == 400


def test_post_curso_tipo_erroneo():
    response = client.post('/cursos/',
                           json={'id_creador': 'Renzo', 'titulo': 'postCurso',
                                 'descripcion': 'descr', 'hashtags': 'hola', 'tipo': 'dsfsdfsd',
                                 'suscripcion': 'gratuito', 'ubicacion': 'virtual'})
    assert response.status_code == 400


def test_post_curso_sin_suscripcion():
    response = client.post('/cursos/',
                           json={'id_creador': 'Renzo', 'titulo': 'postCurso',
                                 'descripcion': 'descr', 'hashtags': 'hola', 'tipo': 'idioma',
                                 'ubicacion': 'virtual'})
    assert response.status_code == 400


def test_post_curso_suscripcion_erronea():
    response = client.post('/cursos/',
                           json={'id_creador': 'Renzo', 'titulo': 'postCurso',
                                 'descripcion': 'descr', 'hashtags': 'hola', 'tipo': 'idioma',
                                 'suscripcion': 'sdfsdfs', 'ubicacion': 'virtual'})
    assert response.status_code == 400


def test_get_cursos():
    response = client.get('/cursos')
    assert response.status_code == 200


def test_get_curso():
    response_post = client.post('/cursos/',
                                json={'id_creador': 'Renzo', 'titulo': 'GetCurso',
                                      'descripcion': 'descr', 'hashtags': 'hola', 'tipo': 'idioma',
                                      'suscripcion': 'gratuito', 'ubicacion': 'virtual'})
    id_post = response_post.json().get('id')
    response = client.get('/cursos/' + id_post)
    assert response.status_code == 200


def test_get_curso_inexistente():
    response = client.get('/cursos/58738aa9-a3ee-4ca9-8b36-4a0c20c1693f')
    assert response.status_code == 404


def test_delete_curso():
    response_post = client.post('/cursos/',
                                json={'id_creador': 'Renzo', 'titulo': 'DeleteCurso',
                                      'descripcion': 'descr', 'hashtags': 'hola', 'tipo': 'idioma',
                                      'suscripcion': 'gratuito', 'ubicacion': 'virtual'})
    id_post = response_post.json().get('id')
    response = client.delete('/cursos/' + id_post)
    assert response.status_code == 200


def test_editar_titulo_curso():
    response_post = client.post('/cursos/',
                                json={'id_creador': 'Renzo', 'titulo': 'EditarTest',
                                      'descripcion': 'descr', 'hashtags': 'hola', 'tipo': 'idioma',
                                      'suscripcion': 'gratuito', 'ubicacion': 'virtual'})
    id_post = response_post.json().get('id')
    response = client.put('/cursos/' + id_post, json={'nuevo_titulo': 'nuevoTitulo'})
    assert response.json().get('titulo') == 'nuevoTitulo' and response.status_code == 200


def test_editar_descripcion_curso():
    response_post = client.post('/cursos/',
                                json={'id_creador': 'Renzo', 'titulo': 'EditarTest',
                                      'descripcion': 'descr', 'hashtags': 'hola', 'tipo': 'idioma',
                                      'suscripcion': 'gratuito', 'ubicacion': 'virtual'})
    id_post = response_post.json().get('id')
    response = client.put('/cursos/' + id_post, json={'nueva_descripcion': 'nuevaDescripcion'})
    assert response.json().get('descripcion') == 'nuevaDescripcion' and response.status_code == 200


def test_editar_estado_valido_curso():
    response_post = client.post('/cursos/',
                                json={'id_creador': 'Renzo', 'titulo': 'EditarTest',
                                      'descripcion': 'descr', 'hashtags': 'hola', 'tipo': 'idioma',
                                      'suscripcion': 'gratuito', 'ubicacion': 'virtual'})
    id_post = response_post.json().get('id')
    response = client.put('/cursos/' + id_post, json={'nuevo_estado': 'bloqueado'})
    assert response.json().get('estado') == 'bloqueado' and response.status_code == 200


def test_editar_estado_invalido_curso():
    response_post = client.post('/cursos/',
                                json={'id_creador': 'Renzo', 'titulo': 'EditarTest',
                                      'descripcion': 'descr', 'hashtags': 'hola', 'tipo': 'idioma',
                                      'suscripcion': 'gratuito', 'ubicacion': 'virtual'})
    id_post = response_post.json().get('id')
    response = client.put('/cursos/' + id_post, json={'nuevo_estado': 'inexistente'})
    assert response.status_code == 400


def test_editar_hashtags_curso():
    response_post = client.post('/cursos/',
                                json={'id_creador': 'Renzo', 'titulo': 'EditarTest',
                                      'descripcion': 'descr', 'hashtags': 'hola', 'tipo': 'idioma',
                                      'suscripcion': 'gratuito', 'ubicacion': 'virtual'})
    id_post = response_post.json().get('id')
    response = client.put('/cursos/' + id_post, json={'nuevos_hashtags': '#h1'})
    assert response.json().get('hashtags') == '#h1' and response.status_code == 200


def test_editar_tipo_valido_curso():
    response_post = client.post('/cursos/',
                                json={'id_creador': 'Renzo', 'titulo': 'EditarTest',
                                      'descripcion': 'descr', 'hashtags': 'hola', 'tipo': 'idioma',
                                      'suscripcion': 'gratuito', 'ubicacion': 'virtual'})
    id_post = response_post.json().get('id')
    response = client.put('/cursos/' + id_post, json={'nuevo_tipo': 'programacion'})
    assert response.json().get('tipo') == 'programacion' and response.status_code == 200


def test_editar_tipo_invalido_curso():
    response_post = client.post('/cursos/',
                                json={'id_creador': 'Renzo', 'titulo': 'EditarTest',
                                      'descripcion': 'descr', 'hashtags': 'hola', 'tipo': 'idioma',
                                      'suscripcion': 'gratuito', 'ubicacion': 'virtual'})
    id_post = response_post.json().get('id')
    response = client.put('/cursos/' + id_post, json={'nuevo_tipo': 'inexistente'})
    assert response.status_code == 400


def test_editar_suscripcion_valida_curso():
    response_post = client.post('/cursos/',
                                json={'id_creador': 'Renzo', 'titulo': 'EditarTest',
                                      'descripcion': 'descr', 'hashtags': 'hola', 'tipo': 'idioma',
                                      'suscripcion': 'gratuito', 'ubicacion': 'virtual'})
    id_post = response_post.json().get('id')
    response = client.put('/cursos/' + id_post, json={'nueva_suscripcion': 'pago'})
    assert response.json().get('suscripcion') == 'pago' and response.status_code == 200


def test_editar_suscripcion_invalida_curso():
    response_post = client.post('/cursos/',
                                json={'id_creador': 'Renzo', 'titulo': 'EditarTest',
                                      'descripcion': 'descr', 'hashtags': 'hola', 'tipo': 'idioma',
                                      'suscripcion': 'gratuito', 'ubicacion': 'virtual'})
    id_post = response_post.json().get('id')
    response = client.put('/cursos/' + id_post, json={'nueva_suscripcion': 'inexistente'})
    assert response.status_code == 400


def test_editar_ubicacion_curso():
    response_post = client.post('/cursos/',
                                json={'id_creador': 'Renzo', 'titulo': 'EditarTest',
                                      'descripcion': 'descr', 'hashtags': 'hola', 'tipo': 'idioma',
                                      'suscripcion': 'gratuito', 'ubicacion': 'virtual'})
    id_post = response_post.json().get('id')
    response = client.put('/cursos/' + id_post, json={'nueva_ubicacion': 'paseo colon'})
    assert response.json().get('ubicacion') == 'paseo colon' and response.status_code == 200


def test_get_cursos_creador_sin_cursos():
    response = client.get('4e4707da-0542-4f9c-ae59-bc3bcaafde71/cursos')
    assert response.status_code == 200


def test_get_cursos_creador_con_cursos():
    client.post('/cursos/',
                json={'id_creador': 'Renzo', 'titulo': 'CursosCreadorTest',
                      'descripcion': 'descr', 'hashtags': 'hola', 'tipo': 'idioma',
                      'suscripcion': 'gratuito', 'ubicacion': 'virtual'})
    response = client.get('fa3333cf-10e2-44df-9bc5-ae4c8d936c66/cursos')
    assert response.status_code == 200


def test_inscribirse_curso():
    response_post = client.post('/cursos/',
                                json={'id_creador': 'hola@gmail.com', 'titulo': 'InscribirseTest',
                                      'descripcion': 'descr', 'hashtags': 'hola', 'tipo': 'idioma',
                                      'suscripcion': 'gratuito', 'ubicacion': 'virtual'})
    id_post = response_post.json().get('id')
    response = client.post('/cursos/' + id_post + '/inscribirse', json={'username': 'admin@admin.com'})
    assert response.status_code == 200


def test_inscribirse_curso_sin_username():
    response_post = client.post('/cursos/',
                                json={'id_creador': 'hola@gmail.com', 'titulo': 'InscribirseTest',
                                      'descripcion': 'descr', 'hashtags': 'hola', 'tipo': 'idioma',
                                      'suscripcion': 'gratuito', 'ubicacion': 'virtual'})
    id_post = response_post.json().get('id')
    response = client.post('/cursos/' + id_post + '/inscribirse', json={})
    assert response.status_code == 400


def test_inscribirse_curso_dos_veces():
    response_post = client.post('/cursos/',
                                json={'id_creador': 'hola@gmail.com', 'titulo': 'InscribirseTest',
                                      'descripcion': 'descr', 'hashtags': 'hola', 'tipo': 'idioma',
                                      'suscripcion': 'gratuito', 'ubicacion': 'virtual'})
    id_post = response_post.json().get('id')
    client.post('/cursos/' + id_post + '/inscribirse', json={'username': 'admin@admin.com'})
    response = client.post('/cursos/' + id_post + '/inscribirse', json={'username': 'admin@admin.com'})
    assert response.status_code == 400


def test_desinscribirse_curso():
    response_post = client.post('/cursos/',
                                json={'id_creador': 'hola@gmail.com', 'titulo': 'DesinscribirseTest',
                                      'descripcion': 'descr', 'hashtags': 'hola', 'tipo': 'idioma',
                                      'suscripcion': 'gratuito', 'ubicacion': 'virtual'})
    id_post = response_post.json().get('id')
    client.post('/cursos/' + id_post + '/inscribirse', json={'username': 'admin@admin.com'})
    response = client.put('/cursos/' + id_post + '/desinscribirse', json={'username': 'admin@admin.com'})
    assert response.json().get('estado') == EstadoCursadaEnum.desinscripto
    assert response.status_code == 200


def test_desinscribirse_curso_inexistente():
    response_post = client.post('/cursos/',
                                json={'id_creador': 'hola@gmail.com', 'titulo': 'DesinscribirseTest',
                                      'descripcion': 'descr', 'hashtags': 'hola', 'tipo': 'idioma',
                                      'suscripcion': 'gratuito', 'ubicacion': 'virtual'})
    id_post = response_post.json().get('id')
    client.post('/cursos/' + id_post + '/inscribirse', json={'username': 'admin@admin.com'})
    response = client.put('/cursos/4311b8ad-9178-403d-9d9b-d9070378b95f/desinscribirse',
                          json={'username': 'admin@admin.com'})
    assert response.status_code == 404


def test_get_listado_de_alumnos_curso_existente():
    response_post = client.post('/cursos/',
                                json={'id_creador': 'hola@gmail.com', 'titulo': 'ListadoTest',
                                      'descripcion': 'descr', 'hashtags': 'hola', 'tipo': 'idioma',
                                      'suscripcion': 'gratuito', 'ubicacion': 'virtual'})
    id_post = response_post.json().get('id')
    client.post('/cursos/' + id_post + '/inscribirse', json={'username': 'admin@admin.com'})
    client.post('/cursos/' + id_post + '/inscribirse', json={'username': 'admin2@admin.com'})
    client.post('/cursos/' + id_post + '/inscribirse', json={'username': 'admin3@admin.com'})
    response = client.get('/cursos/' + id_post + '/alumnos')
    assert response.status_code == 200 and\
           response.json() == ['admin@admin.com', 'admin2@admin.com', 'admin3@admin.com']


def test_get_listado_de_alumnos_curso_inexistente():
    response = client.get('/cursos/c8886379-356d-49f7-8fc2-d6a566a8384d/alumnos')
    assert response.status_code == 404


def test_get_listado_de_alumnos_curso_existente_alumno_desinscripto():
    response_post = client.post('/cursos/',
                                json={'id_creador': 'holaa@gmail.com', 'titulo': 'ListadoDesinscriptoTest',
                                      'descripcion': 'descr', 'hashtags': 'hola', 'tipo': 'idioma',
                                      'suscripcion': 'gratuito', 'ubicacion': 'virtual'})
    id_post = response_post.json().get('id')
    client.post('/cursos/' + id_post + '/inscribirse', json={'username': 'admin11@admin.com'})
    client.post('/cursos/' + id_post + '/inscribirse', json={'username': 'admin12@admin.com'})
    client.post('/cursos/' + id_post + '/inscribirse', json={'username': 'admin13@admin.com'})
    client.put('/cursos/' + id_post + '/desinscribirse', json={'username': 'admin13@admin.com'})

    response = client.get('/cursos/' + id_post + '/alumnos')

    assert response.status_code == 200 and response.json() == ['admin11@admin.com', 'admin12@admin.com']


def test_get_listado_de_alumnos_curso_existente_alumno_inscripto_despues_de_desinscripto():
    response_post = client.post('/cursos/',
                                json={'id_creador': 'holaa@gmail.com',
                                      'titulo': 'ListadoInscriptoDesinscriptoInscriptoTest',
                                      'descripcion': 'descr', 'hashtags': 'hola', 'tipo': 'idioma',
                                      'suscripcion': 'gratuito', 'ubicacion': 'virtual'})
    id_post = response_post.json().get('id')
    client.post('/cursos/' + id_post + '/inscribirse', json={'username': 'admin111@admin.com'})
    client.put('/cursos/' + id_post + '/desinscribirse', json={'username': 'admin111@admin.com'})
    client.post('/cursos/' + id_post + '/inscribirse', json={'username': 'admin111@admin.com'})

    response = client.get('/cursos/' + id_post + '/alumnos')

    assert response.status_code == 200 and response.json() == ['admin111@admin.com']


def test_get_curso_by_tipo():
    response = client.get('/cursos/tipos/?tipo=idioma')
    assert response.status_code == 200


def test_get_curso_by_suscripcion():
    response = client.get('/cursos/suscripciones/?suscripcion=gratuito')
    assert response.status_code == 200


def test_agregar_colaborador():
    response_post = client.post('/cursos/',
                                json={'id_creador': 'hola@gmail.com', 'titulo': 'InscribirseTest',
                                      'descripcion': 'descr', 'hashtags': 'hola', 'tipo': 'idioma',
                                      'suscripcion': 'gratuito', 'ubicacion': 'virtual'})
    id_post = response_post.json().get('id')
    response = client.post('/cursos/colaborador', json={'username': 'admin@admin.com', 'id_curso': id_post})
    assert response.status_code == 200


def test_agregar_colaborador_dos_veces():
    response_post = client.post('/cursos/',
                                json={'id_creador': 'hola@gmail.com', 'titulo': 'InscribirseTest',
                                      'descripcion': 'descr', 'hashtags': 'hola', 'tipo': 'idioma',
                                      'suscripcion': 'gratuito', 'ubicacion': 'virtual'})
    id_post = response_post.json().get('id')
    response_1 = client.post('/cursos/colaborador', json={'username': 'admin@admin.com', 'id_curso': id_post})
    response_2 = client.post('/cursos/colaborador', json={'username': 'admin@admin.com', 'id_curso': id_post})
    assert response_1.status_code == 200
    assert response_2.status_code == 422


def test_crear_examen_exitoso():
    crear_curso_response = client.post('/cursos/',
                                       json={'id_creador': 'hola@gmail.com', 'titulo': 'InscribirseTest',
                                             'descripcion': 'descr', 'hashtags': 'hola', 'tipo': 'idioma',
                                             'suscripcion': 'gratuito', 'ubicacion': 'virtual'})
    id_curso = crear_curso_response.json().get('id')
    crear_examen_response = client.post('/cursos/examen', json={'id_curso': id_curso,
                                                                'nombre': 'test examen',
                                                                'consignas': [
                                                                    {
                                                                        'enunciado': 'Pregunta 1',
                                                                        'puntaje': 4
                                                                    },
                                                                    {
                                                                        'enunciado': 'Pregunta 2',
                                                                        'puntaje': 6
                                                                    }]})
    assert crear_examen_response.status_code == 201


def test_get_examen_exitoso():
    crear_curso_response = client.post('/cursos/',
                                       json={'id_creador': 'hola@gmail.com', 'titulo': 'InscribirseTest',
                                             'descripcion': 'descr', 'hashtags': 'hola', 'tipo': 'idioma',
                                             'suscripcion': 'gratuito', 'ubicacion': 'virtual'})
    id_curso = crear_curso_response.json().get('id')
    crear_examen_response = client.post('/cursos/examen', json={'id_curso': id_curso,
                                                                'nombre': 'test examen',
                                                                'consignas': [
                                                                    {
                                                                        'enunciado': 'Pregunta 1',
                                                                        'puntaje': 4
                                                                    },
                                                                    {
                                                                        'enunciado': 'Pregunta 2',
                                                                        'puntaje': 6
                                                                    }]})
    id_examen = crear_examen_response.json().get('id')
    get_examen_response = client.get(f'/cursos/examen/{id_examen}')

    assert get_examen_response.status_code == 200
    assert get_examen_response.json().get('id') == id_examen


def test_publicar_examen_exitoso():
    crear_curso_response = client.post('/cursos/',
                                       json={'id_creador': 'hola@gmail.com', 'titulo': 'InscribirseTest',
                                             'descripcion': 'descr', 'hashtags': 'hola', 'tipo': 'idioma',
                                             'suscripcion': 'gratuito', 'ubicacion': 'virtual'})
    id_curso = crear_curso_response.json().get('id')
    crear_examen_response = client.post('/cursos/examen', json={'id_curso': id_curso,
                                                                'nombre': 'test examen',
                                                                'consignas': [
                                                                    {
                                                                        'enunciado': 'Pregunta 1',
                                                                        'puntaje': 4
                                                                    },
                                                                    {
                                                                        'enunciado': 'Pregunta 2',
                                                                        'puntaje': 6
                                                                    }]})
    id_examen = crear_examen_response.json().get('id')
    publicar_examen_response = client.post(f'/cursos/examen/publicar/{id_examen}')

    assert publicar_examen_response.status_code == 200
    assert publicar_examen_response.json().get('id') == id_examen
    assert publicar_examen_response.json().get('estado') == EstadoExamenEnum.publicado


def test_update_examen_exitoso():
    crear_curso_response = client.post('/cursos/',
                                       json={'id_creador': 'hola@gmail.com', 'titulo': 'InscribirseTest',
                                             'descripcion': 'descr', 'hashtags': 'hola', 'tipo': 'idioma',
                                             'suscripcion': 'gratuito', 'ubicacion': 'virtual'})
    id_curso = crear_curso_response.json().get('id')
    crear_examen_response = client.post('/cursos/examen', json={'id_curso': id_curso,
                                                                'nombre': 'test examen',
                                                                'consignas': [
                                                                    {
                                                                        'enunciado': 'Pregunta 1',
                                                                        'puntaje': 4
                                                                    },
                                                                    {
                                                                        'enunciado': 'Pregunta 2',
                                                                        'puntaje': 6
                                                                    }]})
    id_examen = crear_examen_response.json().get('id')
    update_examen_response = client.patch(f'/cursos/examen', json={'id': id_examen,
                                                                   'nombre': 'test examen 2',
                                                                   'consignas': [
                                                                    {
                                                                        'enunciado': 'Pregunta 3',
                                                                        'puntaje': 5
                                                                    },
                                                                    {
                                                                        'enunciado': 'Pregunta 4',
                                                                        'puntaje': 5
                                                                    }]})

    assert update_examen_response.status_code == 200
    assert update_examen_response.json().get('id') == id_examen
    assert update_examen_response.json().get('nombre') == 'test examen 2'


def test_crear_examen_resuelto_sin_cursada():
    crear_curso_response = client.post('/cursos/',
                                       json={'id_creador': 'creador@test.com', 'titulo': 'InscribirseTest',
                                             'descripcion': 'descr', 'hashtags': 'hola', 'tipo': 'idioma',
                                             'suscripcion': 'gratuito', 'ubicacion': 'virtual'})
    id_curso = crear_curso_response.json().get('id')
    crear_examen_response = client.post('/cursos/examen', json={'id_curso': id_curso,
                                                                'nombre': 'test examen',
                                                                'consignas': [
                                                                    {
                                                                        'enunciado': 'Pregunta 1',
                                                                        'puntaje': 4
                                                                    },
                                                                    {
                                                                        'enunciado': 'Pregunta 2',
                                                                        'puntaje': 6
                                                                    }]})
    id_examen = crear_examen_response.json().get('id')
    id_consigna_1 = crear_examen_response.json().get('consignas')[0].get('id')
    id_consigna_2 = crear_examen_response.json().get('consignas')[1].get('id')
    crear_examen_resuelto_response = client.post('/cursos/examen_resuelto',
                                                 json={
                                                     'id_examen': id_examen,
                                                     'id_curso': id_curso,
                                                     'username': 'estudiante@test.com',
                                                     'respuestas': [
                                                         {
                                                             'id_consigna': id_consigna_1,
                                                             'resolucion': 'Resolucion 1'
                                                         },
                                                         {
                                                             'id_consigna': id_consigna_2,
                                                             'resolucion': 'Resolucion 2'
                                                         }
                                                     ]
                                                 })
    assert crear_examen_resuelto_response.status_code == 400


def test_crear_examen_resuelto_exitoso():
    crear_curso_response = client.post('/cursos/',
                                       json={'id_creador': 'creador@test.com', 'titulo': 'InscribirseTest',
                                             'descripcion': 'descr', 'hashtags': 'hola', 'tipo': 'idioma',
                                             'suscripcion': 'gratuito', 'ubicacion': 'virtual'})
    id_curso = crear_curso_response.json().get('id')
    client.post('/cursos/' + id_curso + '/inscribirse', json={'username': 'estudiante@test.com'})
    crear_examen_response = client.post('/cursos/examen', json={'id_curso': id_curso,
                                                                'nombre': 'test examen',
                                                                'consignas': [
                                                                    {
                                                                        'enunciado': 'Pregunta 1',
                                                                        'puntaje': 4
                                                                    },
                                                                    {
                                                                        'enunciado': 'Pregunta 2',
                                                                        'puntaje': 6
                                                                    }]})
    id_examen = crear_examen_response.json().get('id')
    id_consigna_1 = crear_examen_response.json().get('consignas')[0].get('id')
    id_consigna_2 = crear_examen_response.json().get('consignas')[1].get('id')
    crear_examen_resuelto_response = client.post('/cursos/examen_resuelto',
                                                 json={
                                                     'id_examen': id_examen,
                                                     'id_curso': id_curso,
                                                     'username': 'estudiante@test.com',
                                                     'respuestas': [
                                                         {
                                                             'id_consigna': id_consigna_1,
                                                             'resolucion': 'Resolucion 1'
                                                         },
                                                         {
                                                             'id_consigna': id_consigna_2,
                                                             'resolucion': 'Resolucion 2'
                                                         }
                                                     ]
                                                 })
    assert crear_examen_resuelto_response.status_code == 201


def test_corregir_examen_resuelto_exitoso():
    crear_curso_response = client.post('/cursos/',
                                       json={'id_creador': 'creador@test.com', 'titulo': 'InscribirseTest',
                                             'descripcion': 'descr', 'hashtags': 'hola', 'tipo': 'idioma',
                                             'suscripcion': 'gratuito', 'ubicacion': 'virtual'})
    id_curso = crear_curso_response.json().get('id')
    client.post('/cursos/' + id_curso + '/inscribirse', json={'username': 'estudiante@test.com'})
    crear_examen_response = client.post('/cursos/examen', json={'id_curso': id_curso,
                                                                'nombre': 'test examen',
                                                                'consignas': [
                                                                    {
                                                                        'enunciado': 'Pregunta 1',
                                                                        'puntaje': 4
                                                                    },
                                                                    {
                                                                        'enunciado': 'Pregunta 2',
                                                                        'puntaje': 6
                                                                    }]})
    id_examen = crear_examen_response.json().get('id')
    id_consigna_1 = crear_examen_response.json().get('consignas')[0].get('id')
    id_consigna_2 = crear_examen_response.json().get('consignas')[1].get('id')
    crear_examen_resuelto_response = client.post('/cursos/examen_resuelto',
                                                 json={
                                                     'id_examen': id_examen,
                                                     'id_curso': id_curso,
                                                     'username': 'estudiante@test.com',
                                                     'respuestas': [
                                                         {
                                                             'id_consigna': id_consigna_1,
                                                             'resolucion': 'Resolucion 1'
                                                         },
                                                         {
                                                             'id_consigna': id_consigna_2,
                                                             'resolucion': 'Resolucion 2'
                                                         }
                                                     ]
                                                 })
    id_examen_resuelto = crear_examen_resuelto_response.json().get('id')
    id_respuesta_1 = crear_examen_resuelto_response.json().get('respuestas')[0].get('id')
    id_respuesta_2 = crear_examen_resuelto_response.json().get('respuestas')[1].get('id')
    corregir_examen_response = client.post('/cursos/examen_resuelto/corregir',
                                           json={
                                               "id_examen_resuelto": id_examen_resuelto,
                                               "corrector": "creador@test.com",
                                               "correcciones": [
                                                   {
                                                       "id_respuesta": id_respuesta_1,
                                                       "es_correcta": True
                                                   },
                                                   {
                                                       "id_respuesta": id_respuesta_2,
                                                       "es_correcta": True
                                                   }
                                               ]
                                           })

    assert corregir_examen_response.status_code == 200
    assert corregir_examen_response.json().get('nota') == 10
    assert corregir_examen_response.json().get('corrector') == 'creador@test.com'
    assert corregir_examen_response.json().get('estado') == EstadoExamenResueltoEnum.corregido


def test_corregir_examen_resuelto_dos_veces():
    crear_curso_response = client.post('/cursos/',
                                       json={'id_creador': 'creador@test.com', 'titulo': 'InscribirseTest',
                                             'descripcion': 'descr', 'hashtags': 'hola', 'tipo': 'idioma',
                                             'suscripcion': 'gratuito', 'ubicacion': 'virtual'})
    id_curso = crear_curso_response.json().get('id')
    client.post('/cursos/' + id_curso + '/inscribirse', json={'username': 'estudiante@test.com'})
    crear_examen_response = client.post('/cursos/examen', json={'id_curso': id_curso,
                                                                'nombre': 'test examen',
                                                                'consignas': [
                                                                    {
                                                                        'enunciado': 'Pregunta 1',
                                                                        'puntaje': 4
                                                                    },
                                                                    {
                                                                        'enunciado': 'Pregunta 2',
                                                                        'puntaje': 6
                                                                    }]})
    id_examen = crear_examen_response.json().get('id')
    id_consigna_1 = crear_examen_response.json().get('consignas')[0].get('id')
    id_consigna_2 = crear_examen_response.json().get('consignas')[1].get('id')
    crear_examen_resuelto_response = client.post('/cursos/examen_resuelto',
                                                 json={
                                                     'id_examen': id_examen,
                                                     'id_curso': id_curso,
                                                     'username': 'estudiante@test.com',
                                                     'respuestas': [
                                                         {
                                                             'id_consigna': id_consigna_1,
                                                             'resolucion': 'Resolucion 1'
                                                         },
                                                         {
                                                             'id_consigna': id_consigna_2,
                                                             'resolucion': 'Resolucion 2'
                                                         }
                                                     ]
                                                 })
    id_examen_resuelto = crear_examen_resuelto_response.json().get('id')
    id_respuesta_1 = crear_examen_resuelto_response.json().get('respuestas')[0].get('id')
    id_respuesta_2 = crear_examen_resuelto_response.json().get('respuestas')[1].get('id')
    corregir_examen_response = client.post('/cursos/examen_resuelto/corregir',
                                           json={
                                               "id_examen_resuelto": id_examen_resuelto,
                                               "corrector": "creador@test.com",
                                               "correcciones": [
                                                   {
                                                       "id_respuesta": id_respuesta_1,
                                                       "es_correcta": True
                                                   },
                                                   {
                                                       "id_respuesta": id_respuesta_2,
                                                       "es_correcta": True
                                                   }
                                               ]
                                           })
    corregir_examen_response_2 = client.post('/cursos/examen_resuelto/corregir',
                                             json={
                                               "id_examen_resuelto": id_examen_resuelto,
                                               "corrector": "creador@test.com",
                                               "correcciones": [
                                                   {
                                                       "id_respuesta": id_respuesta_1,
                                                       "es_correcta": True
                                                   },
                                                   {
                                                       "id_respuesta": id_respuesta_2,
                                                       "es_correcta": True
                                                   }
                                               ]
                                             })
    assert corregir_examen_response_2.status_code == 400
