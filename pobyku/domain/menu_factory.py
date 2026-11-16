from __future__ import annotations

from .interfaces import MenuItemCreator
from .menu_item import MenuItem
from .money import Money


class MenuItemFactory(MenuItemCreator):
    def create(self, item_id: str, name: str, category: str, price_pln: str) -> MenuItem:
        if not item_id or not name or not category:
            raise ValueError("Item id, name and category must be provided")
        price = Money.from_str(price_pln)
        if price < Money.zero():
            raise ValueError("Price cannot be negative")
        return MenuItem(id=item_id, name=name, category=category, price=price)
