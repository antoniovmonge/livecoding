import pytest
from app.main import create_app


@pytest.fixture()
def app():
    app = create_app()

    # other setup can go here

    yield app

    # clean up / reset resources here


@pytest.fixture()
def client(app):
    return app.test_client()
