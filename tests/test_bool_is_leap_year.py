from leap_year_function import *


def test_is_leap_year_when_divisible_by_4_not_100():
    """ Divisible by 4, and not 100"""
    assert bool_is_leap_year(88) is True


def test_leap_year_is_divisible_by_400():
    """If a year is divisible by 400, it's a leap year"""
    assert bool_is_leap_year(400) is True


def test_is_not_leap_year_when_not_divisible_by_four():
    """"""
    assert bool_is_leap_year(5) is False


def test_is_not_leap_year_when_divisible_by_100_not_400():
    """ """
    assert bool_is_leap_year(200) is False


def test_1700_not_leap_year():
    """"""
    assert bool_is_leap_year(1700) is False


def test_2000_is_a_leap_year():
    """"""
    assert bool_is_leap_year(2000) is True
