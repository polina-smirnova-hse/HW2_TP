class Ingredient:
    def __init__(self, name: str, quantity: float, unit: str):
        self.name = name
        self.quantity = quantity
        self.unit = unit
    @property
    def quantity(self):
        return self._quantity
    @quantity.setter
    def quantity(self, x):
        if x <= 0:
            raise ValueError("Количество должно быть положительным")
        if x > 0:
            x = float(x)
            self._quantity = x

    





