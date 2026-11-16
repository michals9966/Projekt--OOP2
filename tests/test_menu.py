from pobyku.domain.interfaces import MenuItemCreator, MenuRepository
from pobyku.domain.menu_factory import MenuItemFactory
from pobyku.domain.menu_item import MenuItem
from pobyku.domain.services import create_default_catalog


class FakeRepository(MenuRepository):
    def __init__(self, items):
        self._items = items

    def get_items(self):
        return self._items


def test_menu_has_required_categories_and_items():
    menu = create_default_catalog()
    categories = menu.get_categories()
    assert len(categories) >= 3
    all_items = []
    for category in categories:
        all_items.extend(menu.get_items_by_category(category))
    assert len(all_items) >= 5


def test_menu_returns_items_for_existing_category():
    menu = create_default_catalog()
    burgers = menu.get_items_by_category("Burgery")
    assert len(burgers) >= 1
    assert all(item.category == "Burgery" for item in burgers)


def test_menu_can_use_custom_repository():
    factory = MenuItemFactory()
    items = [
        factory.create("t1", "Test 1", "TestCat", "10.00"),
        factory.create("t2", "Test 2", "TestCat", "12.00"),
    ]
    from pobyku.domain.menu import Menu

    menu = Menu(FakeRepository(items))
    assert menu.get_categories() == ["TestCat"]
    assert [item.id for item in menu.get_items_by_category("TestCat")] == ["t1", "t2"]
    assert menu.get_item_by_id("t1").name == "Test 1"
