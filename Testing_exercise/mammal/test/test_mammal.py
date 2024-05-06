from unittest import TestCase, main
from project.mammal import Mammal


class MammalTest(TestCase):

    def setUp(self):
        self.mammal = Mammal('Max', 'cat', 'meow')

    def test_correct_initialization(self):
        self.assertEqual('Max', self.mammal.name)
        self.assertEqual('cat', self.mammal.type)
        self.assertEqual('meow', self.mammal.sound)
        self.assertEqual('animals', self.mammal._Mammal__kingdom)

    def test_if_make_sound_is_correct(self):
        expected = "Max makes meow"
        self.assertEqual(expected, self.mammal.make_sound())

    def test_if_get_kingdom_returns_correct_kingdom(self):
        self.assertEqual('animals', self.mammal.get_kingdom())

    def test_if_info_is_correct(self):
        expected = "Max is of type cat"
        self.assertEqual(expected, self.mammal.info())


if __name__ == '__main__':
    main()
