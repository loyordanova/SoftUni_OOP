class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        return 'Making sound'


class Dog(Animal):
    def make_sound(self):
        return super().make_sound() + ' woof-woof'


class Cat(Animal):
    def make_sound(self):
        return super().make_sound() + ' meow'


class Turtle(Animal):
    def make_sound(self):
        return super().make_sound() + ' T sound'


def animal_sound(animals: list):
    for animal in animals:
        print(animal.make_sound())


animals = [Dog('Sharo'), Cat('Tom'), Turtle('Nemo')]
animal_sound(animals)
