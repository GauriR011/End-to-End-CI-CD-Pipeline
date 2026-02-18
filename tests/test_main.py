from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200

def test_add_success():
    response = client.get("/add?a=1&b=2")
    
    assert response.status_code == 200
    assert response.json() == {"result":5} #comparing the returned json response


# def test_add_fail():
#     response = client.get("/add?a=1&b=2")
#     assert response.json() == {"result":6}
