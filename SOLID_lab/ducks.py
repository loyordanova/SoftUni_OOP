from abc import abstractmethod, ABC


class Duck(ABC):

    @staticmethod
    @abstractmethod
    def quack():
        pass


class Fly(ABC):

    @staticmethod
    @abstractmethod
    def fly(self):
        ...


class Walk(ABC):

    @staticmethod
    @abstractmethod
    def walk():
        ...


class RubberDuck(Duck):
    @staticmethod
    def quack():
        return "Squeek"


class RobotDuck(Duck, Fly, Walk):
    HEIGHT = 50

    def __init__(self):
        self.height = 0

    @staticmethod
    def quack():
        return 'Robotic quacking'

    @staticmethod
    def walk():
        return 'Robotic walking'

    def fly(self):
        """can only fly to specific height but
        when it reaches it starts landing automatically"""
        if self.height == RobotDuck.HEIGHT:
            self.land()
        else:
            self.height += 1

    def land(self):
        self.height = 0
