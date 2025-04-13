"""Routes returning snippets for the frontend."""

from flask import Blueprint, jsonify, render_template, request

from isitfiveoclock.openai.client import OpenAIClient

snippets_bp = Blueprint("snippets", __name__, url_prefix="/snippets")


@snippets_bp.route("/get-fact", methods=["GET"])
def get_fact():
    """Return html for the fun fact snippet."""
    # Get the city from the request args
    city = request.args.get("city")
    if not city:
        return "<div>City not provided</div>", 400
    # Check if the city is a string
    if not isinstance(city, str):
        return "<div>Invalid city</div>", 400

    # Get the fun fact from the OpenAI API
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

    # Return the fun fact as html
    return render_template("snippets/fun_fact.html", response=response)
