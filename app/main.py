from os import environ
from datetime import datetime, timedelta

from flask import Flask, jsonify, request, make_response
import jwt


SECRET_KEY = environ.get("SECRET_KEY")


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = SECRET_KEY

    @app.route("/", methods=["GET"])
    def hello_world():
        return jsonify({"message": "Hello, World!"}), 200

    return app


app = create_app()


users_database = [
    {"username": "test_user", "password": "pass1234"},
    {"username": "test_user2", "password": "pass5678"},
]


def user_has_access(func):
    """Decorator to check if user has access to the endpoint"""

    def decorated():
        token = None

        if "Authorization" in request.headers:
            token = request.headers["Authorization"].split()[1]

        if not token:
            return jsonify({"message": "Token is missing"}), 401

        try:
            data = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        except:
            return (
                jsonify(
                    {
                        "message": "Token is invalid, you are not authorized to access this page"
                    }
                ),
                401,
            )

        return func()

    return decorated


@app.route("/login", methods=["POST"])
def login():
    post_data = request.get_json()
    username = post_data.get("username")
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


def user_has_access(func):
    """Decorator to check if user has access to the endpoint"""

    def decorated():
        # Clean the previous token
        token = None

        if "Authorization" in request.headers:
            token = request.headers["Authorization"].split()[1]

        if not token:
            return jsonify({"message": "Token is missing!"}), 401

        try:
            data = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        except:
            return (
                jsonify(
                    {
                        "message": "Token is invalid, \
                        you are not authorized to access this page"
                    }
                ),
                401,
            )
        return func()

    return decorated


@app.route("/private", methods=["GET"])
@user_has_access
def private():
    return (
        jsonify({"message": "This is a private endpoint accessed with a valid token"}),
        200,
    )
