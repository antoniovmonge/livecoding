import os
import jwt


def test_access_without_token(client):
    """Test access to private endpoint without token"""
    response = client.get("/private")
    assert response.status_code == 401
    assert response.get_json() == {"message": "Token is missing"}


def test_access_with_invalid_token(client):
    """Test access to private endpoint with invalid token"""
    response = client.get(
        "/private",
        headers={"Authorization": "Bearer Token is invalid, you are not authorized"},
    )
    assert response.status_code == 401
    assert response.get_json() == {
        "message": "Token is invalid, you are not authorized"
    }


def test_access_with_valid_token(client):
    """Test access to private endpoint with valid token"""
    valid_token = jwt.encode(
        {"some": "payload"}, os.getenv("SECRET_KEY"), algorithm="HS256"
    )
    response = client.get(
        "/private", headers={"Authorization": f"Bearer {valid_token}"}
    )
    assert response.status_code == 200
    assert response.get_json() == {
        "message": "[SUCCESS] This is a private endpoint accessed with a VALID token"
    }
