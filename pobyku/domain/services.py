from __future__ import annotations

from .cart import Cart
from .interfaces import MenuCatalog, MenuItemCreator, MenuRepository, ShoppingCart
from .menu import Menu
from .menu_factory import MenuItemFactory
from .menu_repository import DefaultMenuRepository


def create_default_item_creator() -> MenuItemCreator:
    return MenuItemFactory()


def create_default_menu_repository(item_creator: MenuItemCreator | None = None) -> MenuRepository:
    return DefaultMenuRepository(item_creator or create_default_item_creator())


def create_default_catalog(repository: MenuRepository | None = None) -> MenuCatalog:
    return Menu(repository or create_default_menu_repository())


def create_cart() -> ShoppingCart:
    return Cart()
