import pytest


def to_fahrenheit(c):
    return c * 9 / 5 + 32


def test_freezing():
    assert to_fahrenheit(0) == 32


def test_boiling():
    assert to_fahrenheit(100) == 212
