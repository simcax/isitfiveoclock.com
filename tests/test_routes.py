"""Testing the routes of the Flask application."""


def test_logo(client):
    """Test the logo route."""
    response = client.get("/images/logo.jpg")
    assert response.status_code == 200


def test_get_fact(client):
    """Test the get_fact route."""
    response = client.get("/snippets/get-fact?city=London")
    assert response.status_code == 200
    assert response.data.decode("utf-8") != "<div>City not provided</div>"
    assert response.data.decode("utf-8") != "<div>Invalid city</div>"
    assert response.data.decode("utf-8") != "<div>Error generating fun fact</div>"
    assert "<div>" in response.data.decode("utf-8")
