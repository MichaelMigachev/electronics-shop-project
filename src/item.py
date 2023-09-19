import csv
class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        # Item.all.append(self)

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity

    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate

    @classmethod
    def instantiate_from_csv(cls, file_name):
        """Создание метода класса для открытия файла csv и добавления экземпляров в новый
           список"""
        cls.all = []
        with open(file_name) as f:
            reader = csv.DictReader(f)
            for r in reader:
                cls.all.append(cls(r["name"], r["price"], r["quantity"]))

    @staticmethod
    def string_to_number(string_num):
        """Создание статического метода для возврата числа из строки"""
        if string_num.isdigit():
            return int(string_num)
        return float(string_num) // 1

    @property
    def name(self):
        """Class name getter"""
        return self.__name

    @name.setter
    def name(self, new_name):
        """Class name setter"""
        self.__name = new_name
