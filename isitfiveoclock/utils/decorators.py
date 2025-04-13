"""Modulde containing decorators for the project."""

import os
from functools import wraps

from flask import jsonify, request

BEARER_TOKEN = os.environ.get("API_BEARER_TOKEN")


def token_required(f):
    """Decorator to check for a valid bearer token in the request headers."""

    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get("Authorization")
        if not token or token != f"Bearer {BEARER_TOKEN}":
            return jsonify({"message": "Unauthorized"}), 401
        return f(*args, **kwargs)

    return decorated
