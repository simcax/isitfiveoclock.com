"""Routes for the APi endpoints."""

from flask import Blueprint, jsonify, render_template, request

from isitfiveoclock.openai.client import OpenAIClient

api_bp = Blueprint("api", __name__, url_prefix="/api")


@api_bp.route("/fun-facts", methods=["POST"])
def fun_facts():
    """Endpoint to get fun facts about a city."""
    data = request.get_json()
    prompt = data.get("prompt")
    city = data.get("city")

    if not prompt or not city:
        return jsonify({"message": "Missing prompt or city"}), 400
    if not isinstance(prompt, str) or not isinstance(city, str):
        return jsonify({"message": "Invalid prompt or city"}), 400
    if len(prompt) > 100 or len(city) > 100:
        return jsonify({"message": "Prompt or city too long"}), 400

    # Initialize OpenAI client
    openai_client = OpenAIClient()
    # Generate the prompt for OpenAI
    prompt = f"Give me a fun fact about {city}."
    response = openai_client.query(question=prompt)
    # Check if the response is valid
    if not response:
        return jsonify({"message": "Error generating fun fact"}), 500
    # Return the response
    response = {
        "status": "success",
        "city": city,
        "fun_fact": response,
    }

    return render_template("snippets/fun_fact.html", response=response)
