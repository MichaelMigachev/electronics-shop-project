"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item

def test_Item():
    item = Item("tel", 5000, 2)
    assert item.name == "tel"
    assert item.price == 5000
    assert item.quantity == 2

def test_calculate_total_price():
    item = Item("tel", 5000, 2)
    assert item.calculate_total_price() == 10000

def test_apply_discount():
    item = Item("tel", 5000, 2)
    Item.pay_rate = 0.5
    item.apply_discount()
    assert item.price == 2500
