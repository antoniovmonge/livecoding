import os
from flask import jsonify, request
import jwt


from dotenv import load_dotenv

load_dotenv()


def user_has_access(func):
    """Decorator to check if user has access to the endpoint"""

    def decorated():
        token = None

        if "Authorization" in request.headers:
            token = request.headers["Authorization"].split()[1]

        if not token:
            return jsonify({"message": "Token is missing"}), 401

        try:
            data = jwt.decode(token, os.getenv("SECRET_KEY"), algorithms=["HS256"])
        except:
            return (
                jsonify({"message": "Token is invalid, you are not authorized"}),
                401,
            )

        return func()

    return decorated
