from project.food.dessert import Dessert


class Cake(Dessert):
    GRAMS = 250
    CALORIES = 1000
    PRICE = 5

    def __init__(self, name: str) -> None:
        super().__init__(name, price=self.PRICE, grams=self.GRAMS, calories=self.CALORIES)
