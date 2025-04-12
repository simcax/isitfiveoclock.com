"""Testing the routes of the Flask application."""


def test_logo(client):
    """Test the logo route."""
    response = client.get("/images/logo.jpg")
    assert response.status_code == 200
