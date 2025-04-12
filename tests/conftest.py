"""Common testing fixtures for pytest."""

import pytest

from isitfiveoclock import create_app


@pytest.fixture
def client():
    """Create a test client for the Flask application."""
    app = create_app()
    with app.test_client() as client:
        yield client
