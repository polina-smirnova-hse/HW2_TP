from ingredient import Ingredient
class Recipe:
    def __init__(self, title: str, ingredients: list[Ingredient]):
        self.title = title
        self.ingredients = ingredients
    def add_ingredient(self, ingredient: Ingredient):
        hasIngr = False
        for a in self.ingredients:
            if a == ingredient:
                hsdIngr = True
                ingr = a
        if hasIngr:
            ingr.quantity = ingr.quantity + ingredient.quantity
        if not hasIngr:
            self.ingredients.append(ingredient)
    @staticmethod
    def is_valid_ratio(ratio):
        if ratio > 0 and type(ratio) == float:
            return True
        else:
            return False
    def scale(self, ratio: float):
        if self.is_valid_ratio(ratio):
            for a in self.ingredients:
                a.quantity = a.quantity * ratio
    def __len__(self):
        return len(self.add_ingredient)
    def __str__(self):
        s = ''
        for ingr in self.ingredients:
            s = s + str(ingr) + ", "
        return f"Название блюда: {self.title}, ингредиенты: {s}"