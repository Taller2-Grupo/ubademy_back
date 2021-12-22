from fastapi.testclient import TestClient
from src.main import app, get_db
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.db.database import Base
import os
from dotenv import load_dotenv

load_dotenv()

SQLALCHEMY_DATABASE_URL = os.getenv("TEST_DATABASE_URL")

engine = create_engine(SQLALCHEMY_DATABASE_URL)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base.metadata.create_all(bind=engine)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db


client = TestClient(app)


def test_recomendar_intereses_exitoso():
    recomendar_response = client.get('/recomendaciones/intereses/test@test.com')
    assert recomendar_response.status_code == 200


def test_recomendar_ubicacion_exitoso():
    recomendar_response = client.get('/recomendaciones/ubicacion/test@test.com/10/15')
    assert recomendar_response.status_code == 200
