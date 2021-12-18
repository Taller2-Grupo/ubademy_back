from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)


def test_recomendar_intereses_exitoso():
    recomendar_response = client.get('/recomendaciones/intereses/test@test.com')
    assert recomendar_response.status_code == 200


def test_recomendar_ubicacion_exitoso():
    recomendar_response = client.get('/recomendaciones/ubicacion/10/15')
    assert recomendar_response.status_code == 200
