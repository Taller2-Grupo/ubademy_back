from fastapi.testclient import TestClient
from src.main import app
from src.models.ExamenModel import EstadoExamenEnum
from src.models.ExamenResueltoModel import EstadoExamenResueltoEnum

client = TestClient(app)


def test_crear_examen_exitoso():
    crear_curso_response = client.post('/cursos/',
                                       json={'id_creador': 'hola@gmail.com', 'titulo': 'InscribirseTest',
                                             'descripcion': 'descr', 'hashtags': 'hola', 'tipo': 'idioma',
                                             'suscripcion': 'gratuito', 'ubicacion': 'virtual'})
    id_curso = crear_curso_response.json().get('id')
    crear_examen_response = client.post('/examenes', json={'id_curso': id_curso,
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
    crear_examen_response = client.post('/examenes', json={'id_curso': id_curso,
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
    get_examen_response = client.get(f'/examenes/{id_examen}')

    assert get_examen_response.status_code == 200
    assert get_examen_response.json().get('id') == id_examen


def test_publicar_examen_exitoso():
    crear_curso_response = client.post('/cursos/',
                                       json={'id_creador': 'hola@gmail.com', 'titulo': 'InscribirseTest',
                                             'descripcion': 'descr', 'hashtags': 'hola', 'tipo': 'idioma',
                                             'suscripcion': 'gratuito', 'ubicacion': 'virtual'})
    id_curso = crear_curso_response.json().get('id')
    crear_examen_response = client.post('/examenes',
                                        json={'id_curso': id_curso,
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
    publicar_examen_response = client.post(f'/examenes/publicar/{id_examen}')

    assert publicar_examen_response.status_code == 200
    assert publicar_examen_response.json().get('id') == id_examen
    assert publicar_examen_response.json().get('estado') == EstadoExamenEnum.publicado


def test_update_examen_exitoso():
    crear_curso_response = client.post('/cursos/',
                                       json={'id_creador': 'hola@gmail.com', 'titulo': 'InscribirseTest',
                                             'descripcion': 'descr', 'hashtags': 'hola', 'tipo': 'idioma',
                                             'suscripcion': 'gratuito', 'ubicacion': 'virtual'})
    id_curso = crear_curso_response.json().get('id')
    crear_examen_response = client.post('/examenes', json={'id_curso': id_curso,
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
    update_examen_response = client.patch(f'/examenes', json={'id': id_examen,
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
    crear_examen_response = client.post('/examenes', json={'id_curso': id_curso,
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
    crear_examen_resuelto_response = client.post('/examenes/examenes_resueltos',
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


def test_crear_examen_resuelto_sin_publicar():
    crear_curso_response = client.post('/cursos/',
                                       json={'id_creador': 'creador@test.com', 'titulo': 'InscribirseTest',
                                             'descripcion': 'descr', 'hashtags': 'hola', 'tipo': 'idioma',
                                             'suscripcion': 'gratuito', 'ubicacion': 'virtual'})
    id_curso = crear_curso_response.json().get('id')
    client.post('/cursos/' + id_curso + '/inscribirse', json={'username': 'estudiante@test.com'})
    crear_examen_response = client.post('/examenes', json={'id_curso': id_curso,
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
    crear_examen_resuelto_response = client.post('/examenes/examenes_resueltos',
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
    crear_examen_response = client.post('/examenes', json={'id_curso': id_curso,
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
    publicar_examen_response = client.post(f'/examenes/publicar/{id_examen}')
    crear_examen_resuelto_response = client.post('/examenes/examenes_resueltos',
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
    crear_examen_response = client.post('/examenes', json={'id_curso': id_curso,
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
    publicar_examen_response = client.post(f'/examenes/publicar/{id_examen}')
    crear_examen_resuelto_response = client.post('/examenes/examenes_resueltos',
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
    corregir_examen_response = client.post('/examenes/examenes_resueltos/corregir',
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
    crear_examen_response = client.post('/examenes', json={'id_curso': id_curso,
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
    publicar_examen_response = client.post(f'/examenes/publicar/{id_examen}')
    crear_examen_resuelto_response = client.post('/examenes/examenes_resueltos',
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
    corregir_examen_response = client.post('/examenes/examenes_resueltos/corregir',
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
    corregir_examen_response_2 = client.post('/examenes/examenes_resueltos/corregir',
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


def test_get_examenes_by_curso_2_examenes_creados_busco_todos():
    crear_curso_response = client.post('/cursos/',
                                       json={'id_creador': 'hola@gmail.com', 'titulo': 'InscribirseTest',
                                             'descripcion': 'descr', 'hashtags': 'hola', 'tipo': 'idioma',
                                             'suscripcion': 'gratuito', 'ubicacion': 'virtual'})
    id_curso = crear_curso_response.json().get('id')
    crear_examen_response = client.post('/examenes', json={'id_curso': id_curso,
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
    crear_examen_response_2 = client.post('/examenes', json={'id_curso': id_curso,
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
    get_examenes_by_curso_response = client.get(f'/examenes/curso/{id_curso}')

    assert get_examenes_by_curso_response.status_code == 200
    assert len(get_examenes_by_curso_response.json()) == 2


def test_get_examenes_by_curso_2_examenes_creados_busco_publicados():
    crear_curso_response = client.post('/cursos/',
                                       json={'id_creador': 'hola@gmail.com', 'titulo': 'InscribirseTest',
                                             'descripcion': 'descr', 'hashtags': 'hola', 'tipo': 'idioma',
                                             'suscripcion': 'gratuito', 'ubicacion': 'virtual'})
    id_curso = crear_curso_response.json().get('id')
    crear_examen_response = client.post('/examenes', json={'id_curso': id_curso,
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
    crear_examen_response_2 = client.post('/examenes', json={'id_curso': id_curso,
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
    get_examenes_by_curso_response = client.get(f'/examenes/curso/{id_curso}/?estado=publicado')

    assert get_examenes_by_curso_response.status_code == 200
    assert len(get_examenes_by_curso_response.json()) == 0


def test_get_examenes_by_curso_2_examenes_creados_busco_creados():
    crear_curso_response = client.post('/cursos/',
                                       json={'id_creador': 'hola@gmail.com', 'titulo': 'InscribirseTest',
                                             'descripcion': 'descr', 'hashtags': 'hola', 'tipo': 'idioma',
                                             'suscripcion': 'gratuito', 'ubicacion': 'virtual'})
    id_curso = crear_curso_response.json().get('id')
    crear_examen_response = client.post('/examenes', json={'id_curso': id_curso,
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
    crear_examen_response_2 = client.post('/examenes', json={'id_curso': id_curso,
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
    get_examenes_by_curso_response = client.get(f'/examenes/curso/{id_curso}/?estado=creado')

    assert get_examenes_by_curso_response.status_code == 200
    assert len(get_examenes_by_curso_response.json()) == 2


def test_get_examenes_by_curso_0_examenes():
    crear_curso_response = client.post('/cursos/',
                                       json={'id_creador': 'hola@gmail.com', 'titulo': 'InscribirseTest',
                                             'descripcion': 'descr', 'hashtags': 'hola', 'tipo': 'idioma',
                                             'suscripcion': 'gratuito', 'ubicacion': 'virtual'})
    id_curso = crear_curso_response.json().get('id')
    get_examenes_by_curso_response = client.get(f'/examenes/curso/{id_curso}')

    assert get_examenes_by_curso_response.status_code == 200
    assert len(get_examenes_by_curso_response.json()) == 0


def test_get_examenes_resueltos_by_curso():
    crear_curso_response = client.post('/cursos/',
                                       json={'id_creador': 'creador@test.com', 'titulo': 'InscribirseTest',
                                             'descripcion': 'descr', 'hashtags': 'hola', 'tipo': 'idioma',
                                             'suscripcion': 'gratuito', 'ubicacion': 'virtual'})
    id_curso = crear_curso_response.json().get('id')
    client.post('/cursos/' + id_curso + '/inscribirse', json={'username': 'estudiante@test.com'})
    crear_examen_response = client.post('/examenes', json={'id_curso': id_curso,
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
    publicar_examen_response = client.post(f'/examenes/publicar/{id_examen}')
    crear_examen_resuelto_response_1 = client.post('/examenes/examenes_resueltos',
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
    id_examen_resuelto = crear_examen_resuelto_response_1.json().get('id')
    id_respuesta_1 = crear_examen_resuelto_response_1.json().get('respuestas')[0].get('id')
    id_respuesta_2 = crear_examen_resuelto_response_1.json().get('respuestas')[1].get('id')
    corregir_examen_response = client.post('/examenes/examenes_resueltos/corregir',
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
    client.post('/cursos/' + id_curso + '/inscribirse', json={'username': 'estudiante2@test.com'})
    crear_examen_resuelto_response_2 = client.post('/examenes/examenes_resueltos',
                                                   json={
                                                       'id_examen': id_examen,
                                                       'id_curso': id_curso,
                                                       'username': 'estudiante2@test.com',
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

    get_examenes_todos_response = client.get(f'/examenes/examenes_resueltos/curso/{id_curso}')
    get_examenes_entregados_response = client.get(f'/examenes/examenes_resueltos/curso/{id_curso}/?estado=entregado')
    get_examenes_corregidos_response = client.get(f'/examenes/examenes_resueltos/curso/{id_curso}/?estado=corregido')

    assert get_examenes_todos_response.status_code == 200
    assert len(get_examenes_todos_response.json()) == 2
    assert get_examenes_entregados_response.status_code == 200
    assert len(get_examenes_entregados_response.json()) == 1
    assert get_examenes_corregidos_response.status_code == 200
    assert len(get_examenes_corregidos_response.json()) == 1


def test_get_examenes_resueltos_by_curso_and_username():
    crear_curso_response = client.post('/cursos/',
                                       json={'id_creador': 'creador@test.com', 'titulo': 'InscribirseTest',
                                             'descripcion': 'descr', 'hashtags': 'hola', 'tipo': 'idioma',
                                             'suscripcion': 'gratuito', 'ubicacion': 'virtual'})
    id_curso = crear_curso_response.json().get('id')
    client.post('/cursos/' + id_curso + '/inscribirse', json={'username': 'estudiante@test.com'})
    crear_examen_response = client.post('/examenes', json={'id_curso': id_curso,
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
    publicar_examen_response = client.post(f'/examenes/publicar/{id_examen}')
    crear_examen_resuelto_response_1 = client.post('/examenes/examenes_resueltos',
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
    id_examen_resuelto = crear_examen_resuelto_response_1.json().get('id')
    id_respuesta_1 = crear_examen_resuelto_response_1.json().get('respuestas')[0].get('id')
    id_respuesta_2 = crear_examen_resuelto_response_1.json().get('respuestas')[1].get('id')
    corregir_examen_response = client.post('/examenes/examenes_resueltos/corregir',
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
    client.post('/cursos/' + id_curso + '/inscribirse', json={'username': 'estudiante2@test.com'})
    crear_examen_resuelto_response_2 = client.post('/examenes/examenes_resueltos',
                                                   json={
                                                       'id_examen': id_examen,
                                                       'id_curso': id_curso,
                                                       'username': 'estudiante2@test.com',
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

    get_examenes_estudiante = client.get(f'/examenes/examenes_resueltos/curso/{id_curso}/estudiante@test.com')
    get_examenes_entregados =\
        client.get(f'/examenes/examenes_resueltos/curso/{id_curso}/estudiante@test.com/?estado=entregado')
    get_examenes_estudiante_sin_examenes = \
        client.get(f'/examenes/examenes_resueltos/curso/{id_curso}/estudiante9000@test.com')

    assert get_examenes_estudiante.status_code == 200
    assert len(get_examenes_estudiante.json()) == 1
    assert get_examenes_entregados.status_code == 200
    assert len(get_examenes_entregados.json()) == 0
    assert get_examenes_estudiante_sin_examenes.status_code == 200
    assert len(get_examenes_estudiante_sin_examenes.json()) == 0
