from project.animal import Animal


class Dog(Animal):
    SOUND = 'Woof!'

    def make_sound(self):
        return Dog.SOUND
