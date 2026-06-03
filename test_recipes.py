import sys
sys.path.append("src")
import pytest
from ingredient import Ingredient

def test_ingrCreate():
    ingredient = Ingredient("огурец", 100, "г")
    assert ingredient.name == "огурец"
    assert ingredient.quantity == 100
    assert ingredient.unit == "г"
def test_strr():
    ingredient = Ingredient("помидор", 250, "кг")
    assert str(ingredient) == "помидор: 250.0 кг"
def test_eqq1():
    ingredient1 = Ingredient("помидор", 250, "кг")
    ingredient2 = Ingredient("помидор", 450, "кг")
    assert ingredient1 == ingredient2
def test_eqq2():
    ingredient1 = Ingredient("огурец", 450, "кг")
    ingredient2 = Ingredient("помидор", 450, "кг")
    assert ingredient1 != ingredient2
def test_eqq3():
    ingredient1 = Ingredient("помидор", 450, "г")
    ingredient2 = Ingredient("помидор", 450, "кг")
    assert ingredient1 != ingredient2
    