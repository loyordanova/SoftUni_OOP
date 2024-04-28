from project.cat import Cat


class Tomcat(Cat):
    GENDER = 'Male'
    SOUND = 'Hiss'

    def __init__(self, name, age):
        super().__init__(name, age, gender=Tomcat.GENDER)

    def make_sound(self):
        return Tomcat.SOUND
