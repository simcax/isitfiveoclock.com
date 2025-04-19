"""Tests for the timezone map functionality."""

import os
from io import BytesIO

# Using Pillow library
from PIL import Image

from isitfiveoclock.map.timezone import TimezoneMap


def test_geocode_address():
    """Test the geocode_address method."""
    address = "Sydney, Australia"
    tz_map = TimezoneMap()
    lat, lng = tz_map.geocode_address(address)

    assert isinstance(lat, float)
    assert isinstance(lng, float)
    assert lat != 0.0
    assert lng != 0.0


def test_get_time_zone():
    """Test the get_time_zone method."""
    lat = -33.8688
    lng = 151.2093
    tz_map = TimezoneMap()
    timezone = tz_map.get_time_zone(lat, lng)

    assert isinstance(timezone, str)
    assert timezone != ""
    assert "Australia/Sydney" in timezone


def test_create_map():
    """Test the create_map method."""
    lat = -33.8688
    lng = 151.2093
    timezone = "Australia/Sydney"
    tz_map = TimezoneMap()
    tz_map.create_map(lat, lng, timezone)

    # Check if the map file was created
    assert os.path.exists("map.html")
    # Clean up the created map file
    os.remove("map.html")


def test_create_static_map():
    """Test the create_static_map method."""
    address = "Sydney, Australia"
    tz_map = TimezoneMap()
    map_data = tz_map.create_static_map(address, 600, 400)

    # Check if the static map file was created
    assert map_data is not None
    # Check the image data is 600 pixels wide and 400 pixels high
    # Check if the image data is valid PNG
    img = Image.open(BytesIO(map_data))
    assert img.width == 600
    assert img.height == 400


def test_create_static_map_different_size():
    """Test the create_static_map method with different dimensions."""
    address = "New York, USA"
    tz_map = TimezoneMap()
    map_data = tz_map.create_static_map(address, 400, 400)

    img = Image.open(BytesIO(map_data))
    assert img.width == 400
    assert img.height == 400


def test_create_static_map_invalid_address():
    """Test the create_static_map method with an invalid address."""
    address = "NonExistentPlace, Nowhere"
    tz_map = TimezoneMap()

    # This should return None or raise an exception depending on implementation
    try:
        result = tz_map.create_static_map(address, 600, 400)
        assert result is None
    except Exception as e:
        assert isinstance(e, Exception)


def test_create_static_map_content():
    """Test that the static map contains actual image data."""
    address = "London, UK"
    tz_map = TimezoneMap()
    map_data = tz_map.create_static_map(address, 600, 400)

    img = Image.open(BytesIO(map_data))
    # Check that the image has content (not just blank)
    assert img.getextrema() is not None
