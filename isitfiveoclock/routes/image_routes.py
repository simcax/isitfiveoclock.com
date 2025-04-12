"""Routes for image-related endpoints."""

from flask import Blueprint, send_from_directory

images_bp = Blueprint(
    "images", __name__, url_prefix="/images", template_folder="templates"
)


@images_bp.route("/<path:filename>", methods=["GET"])
def get_image(filename):
    """Serve an image file."""
    return send_from_directory("static/images", filename)
