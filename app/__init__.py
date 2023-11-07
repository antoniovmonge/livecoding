from os import environ
from datetime import datetime, timedelta

from flask import Flask, jsonify, request, make_response
import jwt

from utils.livecoding_decorators import user_has_access
from app.fake_users_database import users_database


SECRET_KEY = environ.get("SECRET_KEY")


def create_app():
    """
    Factory function that creates the Flask app.

    It includes the following endpoints:
    - GET /: Hello World endpoint
    - POST /login: Login endpoint that returns a JWT token
    - GET /private: Private endpoint that requires a valid JWT token to be accessed
    """
    app = Flask(__name__)
    app.config["SECRET_KEY"] = SECRET_KEY

    @app.route("/", methods=["GET"])
    def hello_world():
        return jsonify({"message": "Hello, World!"}), 200

    @app.route("/login", methods=["POST"])
    def login():
        """Login endpoint that returns a JWT token in the headers if the credentials are valid"""
        post_data = request.get_json()
        username = post_data.get("username")
        # The password is not hashed for simplicity of the example
        # In a real application, the password should be always hashed
        password = post_data.get("password")

        for user in users_database:
            if user["username"] == username and user["password"] == password:
                token = jwt.encode(
                    {
                        "sub": username,
                        "iat": datetime.utcnow(),
                        "exp": datetime.utcnow() + timedelta(minutes=30),
                    },
                    SECRET_KEY,
                )
                response = make_response(jsonify({"token": token}))
                response.headers["Bearer"] = token
                return response

        else:
            return jsonify({"message": "Invalid credentials"}), 401

    @app.route("/private", methods=["GET"])
    @user_has_access
    def private():
        return (
            jsonify(
                {
                    "message": "[SUCCESS] This is a private endpoint accessed with a VALID token"
                }
            ),
            200,
        )

    return app


app = create_app()
