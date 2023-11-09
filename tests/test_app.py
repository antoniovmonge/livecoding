"""Test the public route at home page."""


def test_hello_world(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.get_json() == {"message": "Hello, World!"}

# LOGIN TESTS
def test_login(client):
    response = client.post(
        "/login", json={"username": "test_user", "password": "pass1234"}
    )
    assert response.status_code == 200
    assert "Bearer" in response.headers
    assert response.get_json()["token"] is not None


def test_login_invalid_credentials(client):
    response = client.post(
        "/login", json={"username": "test_user", "password": "wrong_password"}
    )
    assert response.status_code == 401
    assert "Bearer" not in response.headers
    assert response.get_json()["message"] == "Invalid credentials"
