from fastapi.testclient import TestClient

from backend.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello":"World"}

def test_read_item():
    item_id = 1
    response = client.get(f"/items/{item_id}")
    expected_result = {"item_id": item_id, "q": None, "detail": "detail-info"}

    assert response.status_code == 200
    assert response.json() == expected_result
