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
def test_shoppingListRemoveNothing():
    ingr = []
    ingr1 = Ingredient("мука", 500, "г")
    ingr.append(ingr1)
    ingr2 = Ingredient("вода", 1, "л")
    ingr.append(ingr2)
    recipe = Recipe("тесто", ingr)
    shopList = ShoppingList()
    shopList.add_recipe(recipe, 1.0)
    shopList.remove_recipe("пицца")
    listOfShops = shopList.get_list()
    assert len(listOfShops) == 2
def test_shoppingListGetListSameIngredients():
    ingr = []
    ingr1 = Ingredient("мука", 500, "г")
    ingr.append(ingr1)
    ingr2 = Ingredient("вода", 1, "л")
    ingr.append(ingr2)
    recipe = Recipe("тесто", ingr)
    shopList = ShoppingList()
    shopList.add_recipe(recipe, 1.0)
    ingrr = []
    ingr11 = Ingredient("мука", 600, "г")
    ingrr.append(ingr11)
    ingr12 = Ingredient("помидоры", 300, "г")
    ingrr.append(ingr12)
    recipe2 = Recipe("пицца", ingrr)
    shopList.add_recipe(recipe2, 1.0)
    listOfShops = shopList.get_list()
    assert len(listOfShops) == 3
    assert listOfShops[1].quantity == 1100
    assert listOfShops[0].name == "вода"
    assert listOfShops[1].name == "мука"
    assert listOfShops[2].name == "помидоры"
def test_shoppingListAddTwoLists():
    ingr = []
    ingr1 = Ingredient("мука", 500, "г")
    ingr.append(ingr1)
    ingr2 = Ingredient("вода", 1, "л")
    ingr.append(ingr2)
    recipe = Recipe("тесто", ingr)
    shopList1 = ShoppingList()
    shopList1.add_recipe(recipe, 1.0)
    list1 = shopList1.get_list()
    ingrr = []
    ingr11 = Ingredient("мука", 600, "г")
    ingrr.append(ingr11)
    ingr12 = Ingredient("помидоры", 300, "г")
    ingrr.append(ingr12)
    recipe2 = Recipe("пицца", ingrr)
    shopList2 = ShoppingList()
    shopList2.add_recipe(recipe2, 1.0)
    list2 = shopList2.get_list()
    new = shopList1 + shopList2
    listOfShops = new.get_list()
    assert len(listOfShops) == 3
    assert listOfShops[0].name == "вода"
    assert listOfShops[1].name == "мука"
    assert listOfShops[2].name == "помидоры"
    assert listOfShops[0].quantity == 1.0
    assert listOfShops[1].quantity == 1100.0
    assert listOfShops[2].quantity == 300.0
def test_shoppingListAddOldLists():
    ingr = []
    ingr1 = Ingredient("мука", 500, "г")
    ingr.append(ingr1)
    ingr2 = Ingredient("вода", 1, "л")
    ingr.append(ingr2)
    recipe = Recipe("тесто", ingr)
    shopList1 = ShoppingList()
    shopList1.add_recipe(recipe, 1.0)
    list1 = shopList1.get_list()
    ingrr = []
    ingr11 = Ingredient("мука", 600, "г")
    ingrr.append(ingr11)
    ingr12 = Ingredient("помидоры", 300, "г")
    ingrr.append(ingr12)
    recipe2 = Recipe("пицца", ingrr)
    shopList2 = ShoppingList()
    shopList2.add_recipe(recipe2, 1.0)
    list2 = shopList2.get_list()
    new = shopList1 + shopList2
    listOfShops = new.get_list()
    assert len(list1) == 2
    assert len(list2) == 2
    assert list1[0].name == "вода"
    assert list1[1].name == "мука"
    assert list1[0].quantity == 1.0
    assert list1[1].quantity == 500.0
    assert list2[0].name == "мука"
    assert list2[1].name == "помидоры"
    assert list2[0].quantity == 600,0
    assert list2[1].quantity == 300.0



    

