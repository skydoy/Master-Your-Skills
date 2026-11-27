import pytest
from cart import Cart


def cart(*prices):
    c = Cart()
    for p in prices:
        c.add("x", p)
    return c


def test_percent():
    c = cart(1999)
    c.apply_code("SAVE10")
    assert c.total() == 1799


def test_flat_floor_zero():
    c = cart(300)
    c.apply_code("FLAT500")
    assert c.total() == 0


def test_replace():
    c = cart(10000)
    c.apply_code("SAVE10")
    c.apply_code("FLAT500")
    assert c.total() == 9500


def test_unknown():
    with pytest.raises(ValueError):
        cart(100).apply_code("NOPE")


def test_discount_follows_later_items():
    c = cart(1000)
    c.apply_code("SAVE10")
    c.add("y", 1000)
    assert c.total() == 1800


def test_no_code():
    assert cart(250, 250).total() == 500
