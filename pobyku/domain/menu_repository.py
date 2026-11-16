from __future__ import annotations

from typing import Sequence

from .interfaces import MenuItemCreator, MenuRepository
from .menu_item import MenuItem


class DefaultMenuRepository(MenuRepository):
    def __init__(self, item_creator: MenuItemCreator) -> None:
        self._item_creator = item_creator

    def get_items(self) -> Sequence[MenuItem]:
        data = [
            ("burger_klasyk", "Klasyk poByku", "Burgery", "32.00"),
            ("burger_serowy", "Serowy Rogacz", "Burgery", "36.00"),
            ("burger_bacon", "Bacon Monster", "Burgery", "38.00"),
            ("burger_ognisty", "Ognisty Byk", "Burgery", "37.00"),
            ("burger_wege", "Zielony Byczek (Wege)", "Burgery", "34.00"),
            ("side_frytki", "Frytki belgijskie grubo cięte", "Dodatki", "12.00"),
            ("side_loaded", "Loaded Fries poByku", "Dodatki", "21.00"),
            ("side_krazki", "Krążki cebulowe (8 szt.)", "Dodatki", "14.00"),
            ("drink_lemoniada", "Domowa lemoniada cytrynowa (400 ml)", "Napoje", "12.00"),
            ("drink_cola", "Cola rzemieślnicza (330 ml)", "Napoje", "10.00"),
            ("drink_woda", "Woda mineralna (500 ml)", "Napoje", "7.00"),
            ("sauce_byk", "Sos Byk (50 ml)", "Sosy", "4.00"),
            ("sauce_bbq", "Sos Dymne BBQ (50 ml)", "Sosy", "4.00"),
            ("sauce_czosnek", "Sos Czosnkowy (50 ml)", "Sosy", "4.00"),
        ]
        return [
            self._item_creator.create(item_id, name, category, price)
            for item_id, name, category, price in data
        ]
