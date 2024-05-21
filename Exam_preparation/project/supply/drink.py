from project.supply.supply import Supply


class Drink(Supply):
    ENERGY: int = 15

    def __init__(self, name):
        super().__init__(name, Drink.ENERGY)

    def details(self) -> str:
        return f"{self.__class__.__name__}: {self.name}, {self.energy}"
