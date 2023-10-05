"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item, InstantiateCSVError
from src.phone import Phone

def test_Item():
    """Тестирование полей класса Item"""
    item = Item("tel", 5000, 2)
    assert item.name == "tel"
    assert item.price == 5000
    assert item.quantity == 2

def test_calculate_total_price():
    """Тестирование метода расчета количества товара"""
    item = Item("tel", 5000, 2)
    assert item.calculate_total_price() == 10000

def test_apply_discount():
    """Тестирование метода применения скидки возвращающий None"""
    item = Item("tel", 5000, 2)
    Item.pay_rate = 0.5
    item.apply_discount()
    assert item.price == 2500

def test_Item_string_to_number():
    """Тестирование @staticmethod string_to_number(...)"""
    assert Item.string_to_number("8") == 8
    assert Item.string_to_number("88.8") == 88

def test_repr():
    """Тест для магических методов  __repr__ и __str__"""
    item1 = Item("Пылесос", 4500, 88)
    item2 = Item('Утюг', 3800, 45)
    assert repr(item1) == "Item('Пылесос', 4500, 88)"
    assert repr(item2) == "Item('Утюг', 3800, 45)"
    assert str(item1) == 'Пылесос'
    assert str(item2) == 'Утюг'


def test_empty_csv():
    """Тестирование пустого файла"""
    with pytest.raises(FileNotFoundError):
        Item.instantiate_from_csv("item.csv")

def test_broken_csv():
    """Тестирование поврежденного файла"""
    with pytest.raises(InstantiateCSVError):
        Item.instantiate_from_csv("items.csv")

