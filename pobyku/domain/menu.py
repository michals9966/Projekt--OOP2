from __future__ import annotations

from .interfaces import MenuCatalog, MenuRepository
from .menu_item import MenuItem


class Menu(MenuCatalog):
    def __init__(self, repository: MenuRepository) -> None:
        self._items = list(repository.get_items())

    def get_categories(self) -> list[str]:
        seen: list[str] = []
        for item in self._items:
            if item.category not in seen:
                seen.append(item.category)
        return seen

    def get_items_by_category(self, category: str) -> list[MenuItem]:
        return [item for item in self._items if item.category == category]

    def get_item_by_id(self, item_id: str) -> MenuItem:
        for item in self._items:
            if item.id == item_id:
                return item
        raise KeyError(f"Menu item not found: {item_id}")
