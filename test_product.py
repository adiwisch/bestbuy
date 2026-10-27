import pytest
from products import Product


def test_create_product():
    """Test that a product can be created successfully."""
    product = Product("MacBook Air M2", price=1450, quantity=100)

    assert product.name == "MacBook Air M2"
    assert product.price == 1450
    assert product.get_quantity() == 100
    assert product.is_active() is True


def test_create_product_with_invalid_details():
    """Test that invalid product details raise exceptions."""

    # Empty name
    with pytest.raises(Exception):
        Product("", price=1450, quantity=100)

    # Negative price
    with pytest.raises(Exception):
        Product("MacBook Air M2", price=-10, quantity=100)


def test_product_becomes_inactive_when_quantity_is_zero():
    """Test that a product becomes inactive when its quantity reaches zero."""
    product = Product("MacBook Air M2", price=1450, quantity=1)

    product.buy(1)

    assert product.get_quantity() == 0
    assert product.is_active() is False


def test_buy_product():
    """Test that buying a product updates its quantity and returns the price."""
    product = Product("MacBook Air M2", price=1450, quantity=100)

    total_price = product.buy(2)

    assert product.get_quantity() == 98
    assert total_price == 2900


def test_buy_more_than_available_quantity():
    """Test that buying more products than available raises an exception."""
    product = Product("MacBook Air M2", price=1450, quantity=5)

    with pytest.raises(Exception):
        product.buy(6)

    assert product.get_quantity() == 5

