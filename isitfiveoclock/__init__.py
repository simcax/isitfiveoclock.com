"""Module to create and configure the Flask application for IsItFiveOClock."""

from os import environ, urandom

from flask import Flask, render_template

from isitfiveoclock.askthetime.whattime import IsItFiveOClock
from isitfiveoclock.routes.api_routes import api_bp
from isitfiveoclock.routes.image_routes import images_bp
from isitfiveoclock.routes.snippet_routes import snippets_bp

app_environment = environ.get("ENVIRONMENT_NAME", "development")
version = environ.get("VERSION")


def create_app(config=None):
    """Create and configure the Flask application."""

    secret_key = str(urandom(12).hex())

    app = Flask(__name__, instance_relative_config=True)

    # Set default configuration
    app.config.from_mapping(
        SECRET_KEY=secret_key,
    )

    # Load config from parameter if provided
    if config is not None:
        if isinstance(config, dict):
            app.config.from_mapping(config)
        else:
            app.config.from_object(config)

    # Try to load the instance config if it exists
    app.config.from_pyfile("config.py", silent=True)

    # Register blueprints
    # from . import routes
    # app.register_blueprint(routes.bp)

    # A simple test route
    @app.route("/hello")
    def hello():
        return "Hello from IsItFiveOClock!"

    @app.route("/")
    def index():
        """Render the home page."""
        # Render the template
        return render_template("index.html")

    @app.route("/isitfiveoclock")
    def isitfiveoclock():
        """Check if it's 5 o'clock somewhere."""
        # Create an instance of IsItFiveOClock
        time_checker = IsItFiveOClock()
        # Get the message
        message, city, country = time_checker.is_it_five_oclock()
        return render_template(
            "isitfiveoclock.html", message=message, city=city, country=country
        )

    @app.route("/version")
    def version_info():
        return f"Version: {version}, Environment: {app_environment}"

    # Error handling
    @app.errorhandler(404)
    def not_found(e):
        return f"Page not found {e}", 404

    @app.errorhandler(500)
    def internal_error(e):
        return f"Internal server error {e}", 500

    app.register_blueprint(images_bp)
    app.register_blueprint(api_bp)
    app.register_blueprint(snippets_bp)
    print(app.url_map)

    return app
