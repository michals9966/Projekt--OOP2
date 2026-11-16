import pytest

from pobyku.domain.menu_factory import MenuItemFactory
from pobyku.domain.money import Money


def test_factory_creates_menu_item_with_correct_data():
    factory = MenuItemFactory()
    item = factory.create("b1", "Klasyk poByku", "Burgery", "32.00")
    assert item.id == "b1"
    assert item.name == "Klasyk poByku"
    assert item.category == "Burgery"
    assert item.price == Money.from_str("32.00")


def test_factory_rejects_negative_price():
    factory = MenuItemFactory()
    with pytest.raises(ValueError):
        factory.create("x1", "Bad item", "Burgery", "-1.00")


def test_factory_rejects_missing_name():
    factory = MenuItemFactory()
    with pytest.raises(ValueError):
        factory.create("x2", "", "Burgery", "10.00")
