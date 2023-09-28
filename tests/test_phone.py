import pytest
from src.phone import Phone

def test_Phone():
    """Тестирование поля кол-ва сим карт класса Phone"""
    phone = Phone("Телефон", 25000, 10, 2)
    assert phone.number_of_sim == 2

def test_repr():
    """Тестирование repr"""
    phone = Phone("Телефон", 25000, 10, 2)
    assert repr(phone) == "Phone('Телефон', 25000, 10, 2)"

def test_setter():
    """Тестирование setter"""
    phone = Phone("Смартфон", 8000, 8, 4)
    phone.number_of_sim = 2
    assert phone.number_of_sim == 2
    phone.number_of_sim = 0
    assert phone.number_of_sim == 2