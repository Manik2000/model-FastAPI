from fastapi.testclient import TestClient
from main import app


client = TestClient(app)

body = {
    "credit_score": 590.0,
    "country": "Spain",
    "gender": "Male",
    "age": 45,
    "tenure": 3,
    "balance": 540.5,
    "products_number": 2,
    "credit_card": 1,
    "active_member": 1,
    "estimated_salary": 4500.89
}

body2 = {
    "credit_score": 590.0,
    "country": "Spain",
    "gender": "Male",
    "age": 45,
    "tenure": 3,
    "balance": 540.5,
    "products_number": 2,
    "credit_card": 1,
    "active_member": 1
}


def test_read_main():
    response = client.post('/score', json=body)
    assert response.status_code == 200


def test_getting_score():
    response = client.post('/score', json=body)
    assert response.json() == {"score": 0.0}


def test_getting_error():
    response = client.post('/score', json=body2)
    assert response.status_code == 422
