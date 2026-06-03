from ingredient import Ingredient
from recipe import Recipe
class ShoppingList:
    def __init__(self):
        self._items = []
    def add_recipe(self, recipe: Recipe, portions: float):
        if portions <= 0:
            raise ValueError("Количество порций должно быть положительным")
        recipe_portions = recipe.scale(portions)
        for ingr in recipe_portions.ingredients:
            self._items.append((ingr, recipe_portions.title))
    def remove_recipe(self, title:str):
        for ingr in self._items:
            if ingr[1] == title:
                self._items.remove(ingr)
    def get_list(self):
        shop = {}
        for ingredient, titles in self._items:
            key = (ingredient.name, ingredient.unit)
            if key in shop.keys():
                quant = shop.get(key)
                new = quant + ingredient.quantity
                shop[key] = new
            else:
                shop[key] = ingredient.quantity
        res = []
        for key in shop.keys():
            res.append(Ingredient(key[0], shop.get(key), key[1]))
        res.sort(key = lambda ingredient: ingredient.name)
        return res
    def __add__(self, other: ShoppingList):
        new = ShoppingList()
        for a in self._items:
            new._items.append(a)
        for a in other._items:
            new._items.append(a)
        return new