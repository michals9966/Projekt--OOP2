import sys
from pathlib import Path

import streamlit as st

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from pobyku.domain.interfaces import MenuCatalog, ShoppingCart
from pobyku.domain.services import create_cart, create_default_catalog


def get_menu() -> MenuCatalog:
    if "menu" not in st.session_state:
        st.session_state.menu = create_default_catalog()
    return st.session_state.menu


def get_cart() -> ShoppingCart:
    if "cart" not in st.session_state:
        st.session_state.cart = create_cart()
    return st.session_state.cart


def main() -> None:
    st.set_page_config(page_title="poByku - Kiosk", layout="wide")
    st.title("Burgerownia poByku")
    st.caption("Etap 2: menu, dodawanie/usuwanie z koszyka, wartość zamówienia")

    menu = get_menu()
    cart = get_cart()

    left, right = st.columns([2, 1], gap="large")

    with left:
        st.subheader("Menu")
        categories = menu.get_categories()
        selected_category = st.selectbox("Kategoria", categories)
        items = menu.get_items_by_category(selected_category)

        for item in items:
            col1, col2, col3 = st.columns([3, 1, 1])
            with col1:
                st.write(f"**{item.name}**")
            with col2:
                st.write(item.price.format_pln())
            with col3:
                if st.button("Dodaj", key=f"add_{item.id}"):
                    cart.add_item(item)
                    st.rerun()

    with right:
        st.subheader("Koszyk")
        entries = cart.get_entries()
        if not entries:
            st.info("Koszyk jest pusty.")
        else:
            for idx, entry in enumerate(entries):
                col1, col2 = st.columns([3, 1])
                with col1:
                    st.write(f"{entry.item.name} — {entry.item.price.format_pln()}")
                with col2:
                    if st.button("Usuń", key=f"remove_{idx}"):
                        cart.remove_item_at(idx)
                        st.rerun()

        st.divider()
        st.markdown(f"**Wartość koszyka: {cart.get_total().format_pln()}**")


if __name__ == "__main__":
    main()
