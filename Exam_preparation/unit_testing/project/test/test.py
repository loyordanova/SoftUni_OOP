

from unittest import TestCase, main

from project.movie import Movie


class TestMovie(TestCase):

    def setUp(self):
        self.movie = Movie('PUFF', 2024, 9)

    def test_initialization(self):
        self.assertEqual('PUFF', self.movie.name)
        self.assertEqual(2024, self.movie.year)
        self.assertEqual(9, self.movie.rating)
        self.assertEqual([], self.movie.actors)

    def test_name_cannot_be_empty_string(self):
        with self.assertRaises(ValueError) as ex:
            self.movie.name = ''
        self.assertEqual("Name cannot be an empty string!", str(ex.exception))

    def test_year_is_not_valid(self):
        with self.assertRaises(ValueError) as ex:
            self.movie.year = 1886
        self.assertEqual("Year is not valid!", str(ex.exception))

    def test_actor_already_added_in_list_of_actors(self):
        self.movie.actors = ['Burya']
        self.assertEqual("Burya is already added in the list of actors!", self.movie.add_actor('Burya'))

    def test_actor_successfully_added(self):
        self.movie.add_actor('Burya')
        self.assertEqual(['Burya'], self.movie.actors)

    def test_rating_is_bigger(self):
        self.other_movie = Movie('HISS', 2023, 8)
        self.assertEqual('"PUFF" is better than "HISS"', self.movie.__gt__(self.other_movie))

    def test_rating_is_smaller(self):
        self.other_movie = Movie('HISS', 2023, 10)
        self.assertEqual('"HISS" is better than "PUFF"', self.movie.__gt__(self.other_movie))

    def test_repr_is_correct(self):
        self.movie.actors = ['Burya', 'Losha']
        expected = f"Name: PUFF\n" \
               f"Year of Release: 2024\n" \
               f"Rating: 9.00\n" \
               f"Cast: Burya, Losha"
        self.assertEqual(expected, self.movie.__repr__())

if __name__ == '__main__':
    main()