"""Tests for integrating with the OpenAI API and prompting facts about cities"""

import os

from isitfiveoclock.openai.client import OpenAIClient


def test_openai_api_key(client):
    """Test if the OpenAI API key is set correctly."""
    question = "What version of OpenAI is current?"
    oa_obj = OpenAIClient()
    response = oa_obj.query(question=question)
    assert len(response) > 1


def test_openai_endpoint(client):
    """Test if the OpenAI API endpoint is reachable."""
    prompt = "Give me a fun fact about London"
    url = "/api/fun-facts"
    bearer_token = os.environ.get("API_BEARER_TOKEN")
    response = client.post(
        url,
        json={
            "prompt": prompt,
            "city": "London",
        },
        headers={"Authorization": f"Bearer {bearer_token}"},
    )
    assert response.status_code == 200
    assert response.json["status"] == "success"
