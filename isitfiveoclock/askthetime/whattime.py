"""Class telling if it's 5 o'clock or not."""

import random
from datetime import datetime

from pytz import timezone


class IsItFiveOClock:
    """Class to determine if it's 5 o'clock somewhere."""

    def __init__(self):
        """Initialize with cities and their timezones."""
        # Cities with timezones (city, country, timezone, drinking_related, fun_fact)
        self.cities = [
            # Cities with drinking-related names
            # pylint: disable=line-too-long
            (
                "Bourbon",
                "USA",
                "US/Eastern",
                True,
                "Bourbon County in Kentucky is known for its bourbon whiskey, which must be aged in new charred oak barrels.",
            ),
            (
                "Whiskey",
                "USA",
                "US/Pacific",
                True,
                "Whiskeytown, California, is named after Whiskeytown Lake, which was created by the Whiskeytown Dam.",
            ),
            (
                "Beer",
                "USA",
                "US/Central",
                True,
                "Beer, Texas, is a small town with a quirky name, but it's also known for its annual beer festival.",
            ),
            (
                "Porto",
                "Portugal",
                "Europe/Lisbon",
                True,
                "Porto is home to the world's oldest wine-producing region, the Douro Valley.",
            ),
            (
                "Cognac",
                "France",
                "Europe/Paris",
                True,
                "Cognac is not only famous for its brandy but also for its unique aging process in Limousin oak barrels.",
            ),
            (
                "Tequila",
                "Mexico",
                "America/Mexico_City",
                True,
                "Tequila is the birthplace of the famous spirit, and the town has a volcano named Tequila Volcano.",
            ),
            (
                "Champagne",
                "France",
                "Europe/Paris",
                True,
                "Champagne can only be called Champagne if it comes from the Champagne region of France.",
            ),
            (
                "Gin",
                "UK",
                "Europe/London",
                True,
                "Gin Lane in London was infamous in the 18th century for its gin shops and the social issues they caused.",
            ),
            (
                "Vodka",
                "Russia",
                "Europe/Moscow",
                True,
                "Vodka is traditionally made from potatoes or grains, and Russia has a museum dedicated to the spirit.",
            ),
            # pylint: disable=line-too-long
            # Regular major cities around the world (covering different timezones)
            (
                "New York",
                "USA",
                "US/Eastern",
                False,
                "New York City has the largest number of billionaires in the world.",
            ),
            # pylint: disable=line-too-long
            (
                "Chicago",
                "USA",
                "US/Central",
                False,
                "Chicago's Willis Tower has retractable glass balconies that extend out from the building.",
            ),
            (
                "Denver",
                "USA",
                "US/Mountain",
                False,
                "Denver is one of the few cities to have a state capitol building made of gold.",
            ),
            (
                "Los Angeles",
                "USA",
                "US/Pacific",
                False,
                "Los Angeles is home to the largest urban oil field in the United States.",
            ),
            (
                "London",
                "UK",
                "Europe/London",
                False,
                "London has a secret underground river called the River Fleet.",
            ),
            (
                "Paris",
                "France",
                "Europe/Paris",
                False,
                "Paris has a hidden vineyard in Montmartre that produces wine.",
            ),
            (
                "Berlin",
                "Germany",
                "Europe/Berlin",
                False,
                "Berlin has more bridges than Venice.",
            ),
            (
                "Moscow",
                "Russia",
                "Europe/Moscow",
                False,
                "Moscow's Kremlin has a secret underground metro system.",
            ),
            (
                "Dubai",
                "UAE",
                "Asia/Dubai",
                False,
                "Dubai has the world's largest flower garden, the Dubai Miracle Garden.",
            ),
            (
                "Mumbai",
                "India",
                "Asia/Kolkata",
                False,
                "Mumbai is home to the world's most expensive private residence, Antilia.",
            ),
            (
                "Tokyo",
                "Japan",
                "Asia/Tokyo",
                False,
                "Tokyo has the world's busiest pedestrian crossing, Shibuya Crossing.",
            ),
            (
                "Sydney",
                "Australia",
                "Australia/Sydney",
                False,
                "Sydney's Opera House has over 1 million tiles on its roof.",
            ),
            (
                "Melbourne",
                "Australia",
                "Australia/Melbourne",
                False,
                "Melbourne was the capital city of Australia for 26 years from 1901 to 1927.",
            ),
            (
                "Brisbane",
                "Australia",
                "Australia/Brisbane",
                False,
                "Brisbane is home to the world's first koala sanctuary, the Lone Pine Koala Sanctuary.",
            ),
            (
                "Perth",
                "Australia",
                "Australia/Perth",
                False,
                "Perth is one of the most isolated major cities in the world, with the nearest city over 2,000km away.",
            ),
            (
                "Auckland",
                "New Zealand",
                "Pacific/Auckland",
                False,
                "Auckland is built on a volcanic field with around 50 volcanoes.",
            ),
            (
                "Rio de Janeiro",
                "Brazil",
                "America/Sao_Paulo",
                False,
                "Rio de Janeiro's Christ the Redeemer statue was struck by lightning in 2014.",
            ),
            (
                "Cape Town",
                "South Africa",
                "Africa/Johannesburg",
                False,
                "Cape Town has a penguin colony at Boulders Beach.",
            ),
            (
                "Beijing",
                "China",
                "Asia/Shanghai",
                False,
                "Beijing's Forbidden City has 9,999 rooms.",
            ),
            (
                "Seoul",
                "South Korea",
                "Asia/Seoul",
                False,
                "Seoul has a theme park dedicated to kimchi.",
            ),
            (
                "Buenos Aires",
                "Argentina",
                "America/Argentina/Buenos_Aires",
                False,
                "Buenos Aires has a bookstore in a former theater, El Ateneo Grand Splendid.",
            ),
            (
                "Cairo",
                "Egypt",
                "Africa/Cairo",
                False,
                "Cairo's Great Pyramid of Giza has a secret chamber.",
            ),
            (
                "Bangkok",
                "Thailand",
                "Asia/Bangkok",
                False,
                "Bangkok's name in Thai is one of the longest place names in the world.",
            ),
            (
                "Jakarta",
                "Indonesia",
                "Asia/Jakarta",
                False,
                "Jakarta is sinking at an alarming rate due to groundwater extraction.",
            ),
            (
                "Lagos",
                "Nigeria",
                "Africa/Lagos",
                False,
                "Lagos has the largest population of any city in Africa.",
            ),
            (
                "Nairobi",
                "Kenya",
                "Africa/Nairobi",
                False,
                "Nairobi is home to the world's only urban national park.",
            ),
            (
                "Santiago",
                "Chile",
                "America/Santiago",
                False,
                "Santiago is surrounded by the Andes mountains, which are visible from the city.",
            ),
            # pylint: disable=line-too-long
            (
                "Havana",
                "Cuba",
                "America/Havana",
                False,
                "Havana has a unique mix of Spanish colonial architecture and Soviet-era buildings.",
            ),
            # pylint: disable=line-too-long
            (
                "Lima",
                "Peru",
                "America/Lima",
                False,
                "Lima is home to the oldest university in the Americas, Universidad Nacional Mayor de San Marcos.",
            ),
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

        for city, country, tz_name, drinking_related, fun_fact in self.cities:
            tz = timezone(tz_name)
            local_time = now.astimezone(tz)

            # Check if it's between 5:00 PM and 5:59 PM local time
            if local_time.hour == 17:
                can_drink = country not in self.alcohol_prohibited
                five_oclock_places.append(
                    (city, country, can_drink, drinking_related, fun_fact)
                )

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
            return "It's always 5 o'clock somewhere, but we couldn't find a specific place right now."

        city, country, can_drink, drinking_related, fun_fact = city_info

        message = f"It's 5 o'clock in {city}, {country}!"

        if not can_drink:
            message += " But unfortunately, alcohol consumption is prohibited there."
        elif drinking_related:
            message += f" With a name like {city}, it sounds like the perfect place for a drink!"
        else:
            message += " Time for a drink!"

        fun_fact = f"{fun_fact}"

        return message, fun_fact
