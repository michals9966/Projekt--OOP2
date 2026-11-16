from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Sequence

from .menu_item import MenuItem
from .money import Money


class MenuItemCreator(ABC):
    @abstractmethod
    def create(self, item_id: str, name: str, category: str, price_pln: str) -> MenuItem:
        raise NotImplementedError


class MenuRepository(ABC):
    @abstractmethod
    def get_items(self) -> Sequence[MenuItem]:
        raise NotImplementedError


class MenuCatalog(ABC):
    @abstractmethod
    def get_categories(self) -> list[str]:
        raise NotImplementedError

    @abstractmethod
    def get_items_by_category(self, category: str) -> list[MenuItem]:
        raise NotImplementedError

    @abstractmethod
    def get_item_by_id(self, item_id: str) -> MenuItem:
        raise NotImplementedError


class ShoppingCart(ABC):
    @abstractmethod
    def add_item(self, item: MenuItem) -> None:
        raise NotImplementedError

    @abstractmethod
    def remove_item_at(self, index: int) -> None:
        raise NotImplementedError

    @abstractmethod
    def get_entries(self) -> list:
        raise NotImplementedError

    @abstractmethod
    def get_total(self) -> Money:
        raise NotImplementedError

    @abstractmethod
    def is_empty(self) -> bool:
        raise NotImplementedError
