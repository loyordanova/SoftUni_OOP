from abc import ABC, abstractmethod


class Chair:
    def __init__(self, name):
        self.name = name


class Sofa:
    def __init__(self, name):
        self.name = name


class Table:
    def __init__(self, name):
        self.name = name


class AbstractFactory(ABC):
    @abstractmethod
    def create_chair(self):
        ...

    @abstractmethod
    def create_sofa(self):
        ...

    @abstractmethod
    def create_table(self):
        ...


class VictorianFactory(AbstractFactory):
    def create_chair(self):
        return Chair('Victorian table')

    def create_table(self):
        return Sofa('Victorian sofa')

    def create_sofa(self):
        return Table('Vivtorian table')


class FuturisticFactory(AbstractFactory):
    def create_chair(self):
        return Chair('Futuristic table')

    def create_table(self):
        return Sofa('Futuristic sofa')

    def create_sofa(self):
        return Table('Futuristic table')


class ModernFactory(AbstractFactory):
    def create_chair(self):
        return Chair('Modern table')

    def create_table(self):
        return Sofa('Modern sofa')

    def create_sofa(self):
        return Table('Modern table')


def get_furniture(style):
    if style == 'victorian':
        factory = VictorianFactory()
    elif style == 'futuristic':
        factory = FuturisticFactory()
    else:
        factory = ModernFactory()

    return factory.create_sofa(), factory.create_chair(), factory.create_table()


request = input()
print(get_furniture(request))