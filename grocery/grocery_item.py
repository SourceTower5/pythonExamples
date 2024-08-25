from enum import Enum

class GroceryType(Enum):
    fruit = 1
    vegetable = 2
    meat = 3
    dairy = 4
    dessert = 5

class GroceryItem:
    def __init__(self, name, price, type):
        self.name = name
        self.price = price
        self.type = type

    @property 
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        self._name = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if not isinstance(value, (int, float)) or value < 0:
            raise ValueError("Price must be a non-negative number")
        self._price = value

    @property
    def type(self):
        return self._type

    @type.setter
    def type(self, value):
        if not isinstance(value, GroceryType):
            raise ValueError("Type must be a GroceryType")
        self._type = value

