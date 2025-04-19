"""Routes returning snippets for the frontend."""

from flask import Blueprint, jsonify, render_template, request
from loguru import logger

from isitfiveoclock.map.timezone import TimezoneMap
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


@snippets_bp.route("/get-map", methods=["GET"])
def get_map():
    """Return html for the map snippet."""
    # Get the screen size of the user
    # Get the screen size from the request args
    width = request.args.get("width", 200)  # Default to 200 if not provided
    height = request.args.get("height", 400)  # Default to 400 if not provided

    # Get the width and height from the request args
    logger.debug(f"Width: {width}, Height: {height}")
    # Log all arguments
    logger.debug(f"Request args: {request.args}")
    # Convert to integers
    try:
        width = int(width)
        height = int(height)
    except (ValueError, TypeError):
        # If conversion fails, use defaults
        width = 200
        height = 400

    # Ensure reasonable limits to prevent extreme sizes
    width = max(100, min(1200, width))  # Between 100 and 1200
    height = max(100, min(1200, height))  # Between 100 and 1200

    # Get the city from the request args
    city = request.args.get("city")
    country = request.args.get("country")
    if not city:
        return "<div>City not provided</div>", 400
    # Check if the city is a string
    if not isinstance(city, str):
        return "<div>Invalid city</div>", 400
    if not country:
        return "<div>country not provided</div>", 400
    tz_map = TimezoneMap()
    # Create the map
    map_data = tz_map.create_static_map(
        city=city,
        country=country,
        map_type="roadmap",
        zoom=1,
        width=300,
        height=400,
    )

    # Return the map as html
    return render_template("snippets/map.html", city=city, map_data=map_data)
