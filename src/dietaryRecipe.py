from recipe import Recipe
class DietaryRecipe(Recipe):
    def __init__(self, title: str, diet_type: str, ingredients = None):
        super().__init__(title, ingredients)
        self.diet_type = diet_type
    def scale(self, ratio: float):
        new = super().scale(ratio)
        newDietRec = DietaryRecipe(self.title, self.diet_type, new.ingredients)
        return newDietRec
    def __str__(self):
        return f"[{self.diet_type}] {super().__str__()}"

