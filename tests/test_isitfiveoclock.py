"""Tests for the isitfiveoclock module."""

from isitfiveoclock.askthetime.whattime import IsItFiveOClock


def test_where_is_it_five_oclock():
    """Test the where_is_it_five_oclock method."""
    instance = IsItFiveOClock()
    result = instance.where_is_it_five_oclock()

    assert isinstance(result, list)
    assert len(result) > 0

    for city_info in result:
        assert isinstance(city_info, tuple)
        assert len(city_info) == 4
        assert isinstance(city_info[0], str)  # city
        assert isinstance(city_info[1], str)  # country
        assert isinstance(city_info[2], bool)  # can_drink
        assert isinstance(city_info[3], bool)  # drinking_related


def test_find_drinking_city():
    """Test the find_drinking_city method."""
    instance = IsItFiveOClock()
    result = instance.find_drinking_city()

    assert isinstance(result, tuple) or result is None

    if result:
        assert len(result) == 4
        assert isinstance(result[0], str)  # city
        assert isinstance(result[1], str)  # country
        assert isinstance(result[2], bool)  # can_drink
        assert isinstance(result[3], bool)  # drinking_related


def test_is_it_five_oclock():
    """Test the is_it_five_oclock method."""
    instance = IsItFiveOClock()
    result = instance.is_it_five_oclock()

    assert isinstance(result, str)
    assert "It's 5 o'clock in" in result or "It's always 5 o'clock somewhere" in result
