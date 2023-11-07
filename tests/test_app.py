import pytest
from app.main import create_app


@pytest.fixture()
def app():
    app = create_app()

    yield app


@pytest.fixture
def client(app):
    with app.test_client() as client:
        yield client


def test_hello_world(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.get_json() == {"message": "Hello, World!"}
