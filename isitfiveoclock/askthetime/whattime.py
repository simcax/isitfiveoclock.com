"""Class telling if it's 5 o'clock or not."""

import random
from datetime import datetime

from loguru import logger
from pytz import timezone


class IsItFiveOClock:
    """Class to determine if it's 5 o'clock somewhere."""

    def __init__(self):
        """Initialize with cities and their timezones."""
        # Cities with timezones (city, country, timezone, drinking_related, fun_fact)
        self.cities = [
            # Cities with drinking-related names
            ("Pierre", "USA", "US/Central", True),
            ("Saint-Pierre", "France", "America/Miquelon", True),
            ("Bourbon", "USA", "US/Eastern", True),
            ("Whiskey", "USA", "US/Pacific", True),
            ("Beer", "USA", "US/Central", True),
            ("Porto", "Portugal", "Europe/Lisbon", True),
            ("Cognac", "France", "Europe/Paris", True),
            ("Tequila", "Mexico", "America/Mexico_City", True),
            ("Champagne", "France", "Europe/Paris", True),
            ("Gin", "UK", "Europe/London", True),
            ("Vodka", "Russia", "Europe/Moscow", True),
            ("Rum", "Jamaica", "America/Jamaica", True),
            ("Scotch", "UK", "Europe/London", True),
            ("Sake", "Japan", "Asia/Tokyo", True),
            ("Margarita", "USA", "US/Central", True),
            ("Heineken", "Netherlands", "Europe/Amsterdam", True),
            # Regular major cities with different timezones
            # North America
            ("New York", "USA", "US/Eastern", False),
            ("Boston", "USA", "US/Eastern", False),
            ("Miami", "USA", "US/Eastern", False),
            ("Atlanta", "USA", "US/Eastern", False),
            ("Chicago", "USA", "US/Central", False),
            ("Dallas", "USA", "US/Central", False),
            ("Houston", "USA", "US/Central", False),
            ("New Orleans", "USA", "US/Central", False),
            ("Denver", "USA", "US/Mountain", False),
            ("Phoenix", "USA", "US/Mountain", False),
            ("Salt Lake City", "USA", "US/Mountain", False),
            ("Los Angeles", "USA", "US/Pacific", False),
            ("San Francisco", "USA", "US/Pacific", False),
            ("Seattle", "USA", "US/Pacific", False),
            ("Vancouver", "Canada", "America/Vancouver", False),
            ("Toronto", "Canada", "America/Toronto", False),
            ("Montreal", "Canada", "America/Montreal", False),
            # Europe
            ("London", "UK", "Europe/London", False),
            ("Manchester", "UK", "Europe/London", False),
            ("Edinburgh", "UK", "Europe/London", False),
            ("Paris", "France", "Europe/Paris", False),
            ("Nice", "France", "Europe/Paris", False),
            ("Lyon", "France", "Europe/Paris", False),
            ("Berlin", "Germany", "Europe/Berlin", False),
            ("Munich", "Germany", "Europe/Berlin", False),
            ("Hamburg", "Germany", "Europe/Berlin", False),
            ("Madrid", "Spain", "Europe/Madrid", False),
            ("Barcelona", "Spain", "Europe/Madrid", False),
            ("Rome", "Italy", "Europe/Rome", False),
            ("Milan", "Italy", "Europe/Rome", False),
            ("Venice", "Italy", "Europe/Rome", False),
            ("Moscow", "Russia", "Europe/Moscow", False),
            ("St. Petersburg", "Russia", "Europe/Moscow", False),
            ("Athens", "Greece", "Europe/Athens", False),
            ("Amsterdam", "Netherlands", "Europe/Amsterdam", False),
            ("Stockholm", "Sweden", "Europe/Stockholm", False),
            ("Oslo", "Norway", "Europe/Oslo", False),
            ("Helsinki", "Finland", "Europe/Helsinki", False),
            ("Lisbon", "Portugal", "Europe/Lisbon", False),
            # Asia
            ("Dubai", "UAE", "Asia/Dubai", False),
            ("Abu Dhabi", "UAE", "Asia/Dubai", False),
            ("Mumbai", "India", "Asia/Kolkata", False),
            ("New Delhi", "India", "Asia/Kolkata", False),
            ("Bangalore", "India", "Asia/Kolkata", False),
            ("Tokyo", "Japan", "Asia/Tokyo", False),
            ("Osaka", "Japan", "Asia/Tokyo", False),
            ("Kyoto", "Japan", "Asia/Tokyo", False),
            ("Shanghai", "China", "Asia/Shanghai", False),
            ("Beijing", "China", "Asia/Shanghai", False),
            ("Hong Kong", "China", "Asia/Hong_Kong", False),
            ("Seoul", "South Korea", "Asia/Seoul", False),
            ("Bangkok", "Thailand", "Asia/Bangkok", False),
            ("Singapore", "Singapore", "Asia/Singapore", False),
            ("Jakarta", "Indonesia", "Asia/Jakarta", False),
            ("Kuala Lumpur", "Malaysia", "Asia/Kuala_Lumpur", False),
            # Australia/Oceania
            ("Sydney", "Australia", "Australia/Sydney", False),
            ("Melbourne", "Australia", "Australia/Melbourne", False),
            ("Brisbane", "Australia", "Australia/Brisbane", False),
            ("Perth", "Australia", "Australia/Perth", False),
            ("Adelaide", "Australia", "Australia/Adelaide", False),
            ("Auckland", "New Zealand", "Pacific/Auckland", False),
            ("Wellington", "New Zealand", "Pacific/Auckland", False),
            ("Christchurch", "New Zealand", "Pacific/Auckland", False),
            # PONT Timezone (UTC+11)
            ("Palikir", "Micronesia", "Pacific/Ponape", False),
            ("Kolonia", "Micronesia", "Pacific/Ponape", False),
            ("Pohnpei", "Micronesia", "Pacific/Ponape", False),
            ("Weno", "Micronesia", "Pacific/Ponape", False),
            ("Yangon", "Myanmar", "Asia/Yangon", False),
            ("Kathmandu", "Nepal", "Asia/Kathmandu", False),
            # South America
            ("Rio de Janeiro", "Brazil", "America/Sao_Paulo", False),
            ("Sao Paulo", "Brazil", "America/Sao_Paulo", False),
            ("Buenos Aires", "Argentina", "America/Argentina/Buenos_Aires", False),
            ("Santiago", "Chile", "America/Santiago", False),
            ("Lima", "Peru", "America/Lima", False),
            ("Bogota", "Colombia", "America/Bogota", False),
            ("Caracas", "Venezuela", "America/Caracas", False),
            # Africa
            ("Cairo", "Egypt", "Africa/Cairo", False),
            ("Cape Town", "South Africa", "Africa/Johannesburg", False),
            ("Johannesburg", "South Africa", "Africa/Johannesburg", False),
            ("Lagos", "Nigeria", "Africa/Lagos", False),
            ("Nairobi", "Kenya", "Africa/Nairobi", False),
            ("Casablanca", "Morocco", "Africa/Casablanca", False),
            ("Dakar", "Senegal", "Africa/Dakar", False),
            # Caribbean/Central America
            ("Havana", "Cuba", "America/Havana", False),
            ("Mexico City", "Mexico", "America/Mexico_City", False),
            ("Panama City", "Panama", "America/Panama", False),
            ("Kingston", "Jamaica", "America/Jamaica", False),
        ]

        # Countries where alcohol is prohibited
        self.alcohol_prohibited = [
            "Saudi Arabia",
            "Iran",
            "Kuwait",
            "Libya",
            "Sudan",
            "Yemen",
            "Bangladesh",
            "Brunei",
            "Pakistan",
            "Mauritania",
            "Somalia",
        ]

    def where_is_it_five_oclock(self) -> list:
        """Find locations where it's currently 5 PM."""
        now = datetime.now()
        five_oclock_places = []

        for city, country, tz_name, drinking_related in self.cities:
            tz = timezone(tz_name)
            local_time = now.astimezone(tz)

            # Check if it's between 5:00 PM and 5:59 PM local time
            if local_time.hour == 17:
                can_drink = country not in self.alcohol_prohibited
                five_oclock_places.append((city, country, can_drink, drinking_related))
        # Log warning if no places found
        if not five_oclock_places or len(five_oclock_places) == 0:
            logger.warning("No places found where it's currently 5 PM.")
            logger.info(f"Current time: {now}, timezone: {tz_name}")

        return five_oclock_places

    def find_drinking_city(self) -> tuple:
        """Find a random city where it's 5 PM."""
        places = self.where_is_it_five_oclock()

        if not places:
            return None

        # Simply return a random city from all places where it's 5 PM
        return random.choice(places)

    def is_it_five_oclock(self) -> str:
        """Get message about where it's 5 PM and if drinking is allowed."""
        city_info = self.find_drinking_city()

        if not city_info:
            # pylint: disable=line-too-long
            return (
                "It's always 5 o'clock somewhere, but we couldn't find a specific place right now."
            ), "unknown"

        city, country, can_drink, drinking_related = city_info

        message = f"It's 5 o'clock in {city}, {country}!"

        if not can_drink:
            message += " But unfortunately, alcohol consumption is prohibited there."
        elif drinking_related:
            message += f" With a name like {city}, it sounds like the perfect place for a drink!"
        else:
            message += " Time for a drink!"

        return message, city, country
