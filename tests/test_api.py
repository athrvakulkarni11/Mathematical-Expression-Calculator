from fastapi.testclient import TestClient
from src.expression_api import app

client = TestClient(app)

def test_evaluate_valid_expression():
    response = client.post(
        "/evaluate",
        json={"expression": "2 + 2"}
    )
    assert response.status_code == 200
    assert response.json() == {"expression": "2 + 2", "result": 4}

def test_evaluate_invalid_expression():
    response = client.post(
        "/evaluate",
        json={"expression": "2 +"}
    )
    assert response.status_code == 400

def test_evaluate_division_by_zero():
    response = client.post(
        "/evaluate",
        json={"expression": "1/0"}
    )
    assert response.status_code == 400 