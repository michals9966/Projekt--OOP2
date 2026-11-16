from __future__ import annotations

from dataclasses import dataclass

from .interfaces import ShoppingCart
from .menu_item import MenuItem
from .money import Money


@dataclass(frozen=True)
class CartEntry:
    item: MenuItem


class Cart(ShoppingCart):
    def __init__(self) -> None:
        self._entries: list[CartEntry] = []

    def add_item(self, item: MenuItem) -> None:
        if item is None:
            raise ValueError("Cannot add empty item to cart")
        self._entries.append(CartEntry(item=item))

    def remove_item_at(self, index: int) -> None:
        if index < 0 or index >= len(self._entries):
            raise IndexError("Cart item index out of range")
        del self._entries[index]

    def get_entries(self) -> list[CartEntry]:
        return list(self._entries)

    def get_total(self) -> Money:
        total = Money.zero()
        for entry in self._entries:
            total = total + entry.item.price
        return total

    def is_empty(self) -> bool:
        return len(self._entries) == 0
