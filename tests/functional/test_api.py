import os 
import io
import tempfile 

import pytest

from main import app

@pytest.fixture()
def client():
    
    app.config.update({"Testing": True})
    client = app.test_client()

    yield client


def test_request_withoutData(client):
    response = client.post("/api/v1/classify", data={
        
    },content_type="multipart/form-data")
    assert response.status_code == 400

def test_request_noFile(client):
    response = client.post("/api/v1/classify", data={
      "image": ""    
    },content_type="multipart/form-data")
    assert response.status_code == 400


def test_request_wrongKey(client):
    response = client.post("/api/v1/classify", data={
      "file": "image.png"    
    },content_type="multipart/form-data")
    assert response.status_code == 400

def test_request_correctKey(client):
    
    file_path = 'tests/test_assets/Allure 3 Piece Sofa and Armchair Set.jpg'
    file_path = os.path.join(os.getcwd(), file_path)

    image = open(file_path, "rb")
    data = {"image": (image, "image.jpg")}
        
    response = client.post("/api/v1/classify",data=data, buffered=True,content_type="multipart/form-data",)
    assert response.status_code == 200

def test_request_wrongExtension(client):
    response = client.post("/api/v1/classify", data={
      "image": ""    
    },content_type="multipart/form-data")
    assert response.status_code == 400