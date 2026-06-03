from ingredient import Ingredient
class Recipe:
    def __init__(self, title: str, ingredients: list[Ingredient]):
        self.title = title
        self.ingredients = ingredients
    def add_ingredient(self, ingredient: Ingredient):
        hasIngr = False
        for a in self.ingredients:
            if a == ingredient:
                hasIngr = True
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
        new = []
        if self.is_valid_ratio(ratio):
            for a in self.ingredients:
                newQuant = a.quantity * ratio
                newIngr = Ingredient(a.name, newQuant, a.unit)
                new.append(newIngr)
            return Recipe(self.title, new)
        else:
            raise ValueError()
    def __len__(self):
        return len(self.ingredients)
    def __str__(self):
        s = ''
        for ingr in self.ingredients:
            s = s + str(ingr) + ", "
        return f"Название блюда: {self.title}, ингредиенты: {s}"