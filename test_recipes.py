import sys
sys.path.append("src")
import pytest
from ingredient import Ingredient
from recipe import Recipe
from shoppingList import ShoppingList

def test_ingrCreate():
    ingredient = Ingredient("огурец", 100, "г")
    assert ingredient.name == "огурец"
    assert ingredient.quantity == 100
    assert ingredient.unit == "г"
def test_ingrStr():
    ingredient = Ingredient("помидор", 250, "кг")
    assert str(ingredient) == "помидор: 250.0 кг"
def test_ingrEqDifferentQuantity():
    ingredient1 = Ingredient("помидор", 250, "кг")
    ingredient2 = Ingredient("помидор", 450, "кг")
    assert ingredient1 == ingredient2
def test_ingrEqDifferentNames():
    ingredient1 = Ingredient("огурец", 450, "кг")
    ingredient2 = Ingredient("помидор", 450, "кг")
    assert ingredient1 != ingredient2
def test_ingrEqDifferentUnits():
    ingredient1 = Ingredient("помидор", 450, "г")
    ingredient2 = Ingredient("помидор", 450, "кг")
    assert ingredient1 != ingredient2

def test_recipeCreate():
    ingr = []
    ingr1 = Ingredient("мука", 500, "г")
    ingr.append(ingr1)
    ingr2 = Ingredient("вода", 1, "л")
    ingr.append(ingr2)
    recipe = Recipe("тесто", ingr)
    assert recipe.title == "тесто"
    assert recipe.ingredients == ingr
def test_recipeAdd():
    ingr = []
    ingrAssert = []
    ingr1 = Ingredient("мука", 500, "г")
    ingr.append(ingr1)
    ingrAssert.append(ingr1)
    ingr2 = Ingredient("вода", 1, "л")
    ingr.append(ingr2)
    ingrAssert.append(ingr2)
    recipe = Recipe("тесто", ingr)
    ingr3 = Ingredient("соль", 5, "г")
    recipe.add_ingredient(ingr3)
    ingrAssert.append(ingr3)
    assert recipe.ingredients == ingrAssert
    assert len(recipe.ingredients) == 3
def test_recipeAddRepeat():
    ingr = []
    ingr1 = Ingredient("мука", 500, "г")
    ingr.append(ingr1)
    ingr2 = Ingredient("вода", 1, "л")
    ingr.append(ingr2)
    recipe = Recipe("тесто", ingr)
    ingr3 = Ingredient("мука", 600, "г")
    recipe.add_ingredient(ingr3)
    assert recipe.ingredients[0].quantity == 1100
    assert recipe.ingredients == ingr
def test_recipeScale():
    ingr = []
    ingr1 = Ingredient("мука", 500, "г")
    ingr.append(ingr1)
    ingr2 = Ingredient("вода", 1, "л")
    ingr.append(ingr2)
    recipe = Recipe("тесто", ingr)
    new = recipe.scale(3.0)
    assert new is not recipe
def test_recipeScaleIncrease():
    ingr = []
    ingr1 = Ingredient("мука", 500, "г")
    ingr.append(ingr1)
    ingr2 = Ingredient("вода", 1, "л")
    ingr.append(ingr2)
    recipe = Recipe("тесто", ingr)
    new = recipe.scale(3.0)
    assert new.ingredients[0].quantity == 1500
    assert new.ingredients[1].quantity == 3
def test_recipeScaleNegativeRatio():
    ingr = []
    ingr1 = Ingredient("мука", 500, "г")
    ingr.append(ingr1)
    ingr2 = Ingredient("вода", 1, "л")
    ingr.append(ingr2)
    recipe = Recipe("тесто", ingr)
    with pytest.raises(ValueError):
        recipe.scale(-1)

def test_shoppingListAdd():
    ingr = []
    ingr1 = Ingredient("мука", 500, "г")
    ingr.append(ingr1)
    ingr2 = Ingredient("вода", 1, "л")
    ingr.append(ingr2)
    recipe = Recipe("тесто", ingr)
    shopList = ShoppingList()
    shopList.add_recipe(recipe, 1.0)
    listOfShops = shopList.get_list()
    assert listOfShops[0].name == "вода"
    assert listOfShops[1].name == "мука"
    assert listOfShops[0].quantity == 1.0
    assert listOfShops[1].quantity == 500.0
def test_shoppingListNegativePortions():
    ingr = []
    ingr1 = Ingredient("мука", 500, "г")
    ingr.append(ingr1)
    ingr2 = Ingredient("вода", 1, "л")
    ingr.append(ingr2)
    recipe = Recipe("тесто", ingr)
    shopList = ShoppingList()
    with pytest.raises(ValueError):
        shopList.add_recipe(recipe, 0)
def test_shoppingListRemove():
    ingr = []
    ingr1 = Ingredient("мука", 500, "г")
    ingr.append(ingr1)
    ingr2 = Ingredient("вода", 1, "л")
    ingr.append(ingr2)
    recipe = Recipe("тесто", ingr)
    shopList = ShoppingList()
    shopList.add_recipe(recipe, 1.0)
    shopList.remove_recipe("тесто")
    listOfShops = shopList.get_list()
    assert len(listOfShops) == 0