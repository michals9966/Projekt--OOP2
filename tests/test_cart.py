import pytest

from pobyku.domain.menu_factory import MenuItemFactory
from pobyku.domain.money import Money
from pobyku.domain.services import create_cart


def make_item(item_id="b1", name="Burger", category="Burgery", price="32.00"):
    return MenuItemFactory().create(item_id, name, category, price)


def test_cart_adds_item_and_updates_total():
    cart = create_cart()
    cart.add_item(make_item())
    assert len(cart.get_entries()) == 1
    assert cart.get_total() == Money.from_str("32.00")


def test_cart_removes_item_by_index():
    cart = create_cart()
    cart.add_item(make_item("b1", "Burger 1", "Burgery", "32.00"))
    cart.add_item(make_item("d1", "Frytki", "Dodatki", "12.00"))
    cart.remove_item_at(0)
    assert len(cart.get_entries()) == 1
    assert cart.get_entries()[0].item.id == "d1"
    assert cart.get_total() == Money.from_str("12.00")


def test_cart_total_is_exact_with_decimal_prices():
    cart = create_cart()
    cart.add_item(make_item("i1", "A", "Sosy", "1.10"))
    cart.add_item(make_item("i2", "B", "Sosy", "2.20"))
    assert cart.get_total() == Money.from_str("3.30")


def test_cart_remove_invalid_index_raises():
    cart = create_cart()
    with pytest.raises(IndexError):
        cart.remove_item_at(0)
