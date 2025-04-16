"""Class for creating a timezone map."""

import base64
import os
import time
from urllib.parse import quote

import folium
import requests

# Replace with your actual API key
API_KEY = os.environ.get("GOOGLE_MAPS_API_KEY")
if API_KEY is None:
    raise ValueError("Google Maps API key not found in environment variables.")


class TimezoneMap:
    def geocode_address(self, address):
        url = f"https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={API_KEY}"
        response = requests.get(url)
        data = response.json()
        if data["status"] == "OK":
            location = data["results"][0]["geometry"]["location"]
            return location["lat"], location["lng"]
        else:
            raise Exception("Geocoding failed")

    def get_time_zone(self, lat, lng):
        timestamp = int(time.time())
        url = f"https://maps.googleapis.com/maps/api/timezone/json?location={lat},{lng}&timestamp={timestamp}&key={API_KEY}"
        response = requests.get(url)
        data = response.json()
        if data["status"] == "OK":
            return data["timeZoneId"]
        else:
            raise Exception("Time Zone API failed")

    def create_map(self, lat, lng, timezone):
        map_ = folium.Map(location=[lat, lng], zoom_start=10)
        folium.Marker([lat, lng], popup=f"Timezone: {timezone}").add_to(map_)
        map_.save("map.html")

    def create_static_map(
        self,
        city: str,
        country: str,
        width: int,
        height: int,
        zoom: int = 5,
        map_type: str = "roadmap",
        marker_color: str = "red",
    ):
        # Geocode the address to get latitude and longitude
        address = f"{city}, {country}"
        geocode_url = f"https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={API_KEY}"
        geocode_response = requests.get(geocode_url)
        geocode_data = geocode_response.json()
        if geocode_data["status"] == "OK":
            location = geocode_data["results"][0]["geometry"]["location"]
            lat, lng = location["lat"], location["lng"]
        else:
            raise Exception("Geocoding failed")

        # Create the static map URL
        # Calculate a shifted center to position the marker in the right third
        # Adjust longitude based on zoom level - higher zoom needs smaller offset
        longitude_shift = 560 / (
            2 ** (zoom + 2)
        )  # Appropriate shift based on zoom level
        shifted_lng = (
            lng - longitude_shift
        )  # Shift center left, placing marker on right third
        # Adjust the latitude based on zoom level, so the marker is higher up in the map
        latitude_shift = -150 / (2 ** (zoom + 2))
        shifted_lat = lat + latitude_shift
        # Set the label text for the marker
        label_text = quote("5")
        # Create the static map URL
        static_map_url = f"https://maps.googleapis.com/maps/api/staticmap?center={shifted_lat},{shifted_lng}&zoom={zoom}&size={width}x{height}&maptype={map_type}&markers=color:{marker_color}%7Clabel:{label_text}%7C{lat},{lng}&key={API_KEY}"

        # Fetch the static map image
        response = requests.get(static_map_url)

        if response.status_code == 200:
            # Base64 encode the image data
            image_data = base64.b64encode(response.content).decode("utf-8")
            return image_data
        else:
            raise Exception("Failed to fetch the static map")
