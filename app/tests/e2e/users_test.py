# coding=utf-8

from fastapi.testclient import TestClient

from backend.infrastractures.postgres import get_db_context
from backend.models.user_model import UserModel

from backend.main import app

client = TestClient(app)

def test_get_user():
    db_context = get_db_context()
    with db_context as db:
        test_user = UserModel(nickname="test-nickname", email='test@example.com')
        db.add(test_user)
        db.commit()

        user_id = test_user.id
        response = client.get(f"/users/{user_id}")
        actual = response.json()

        assert response.status_code == 200
        assert type(actual['id']) == int
        assert actual['nickname'] == 'test-nickname'
        assert actual['email'] == 'test@example.com'

        db.delete(test_user)
        db.commit()
