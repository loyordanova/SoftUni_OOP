from project.animal import Animal


class Cat(Animal):
    SOUND = 'Meow meow!'

    def make_sound(self):
        return Cat.SOUND
