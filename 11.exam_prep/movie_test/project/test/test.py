from unittest import TestCase, main
from project.movie import Movie


class TestMovie(TestCase):
    def setUp(self):
        self.movie = Movie('Bad Boys', 2000, 5.0)
        self.movie_2 = Movie('Bad Boys 2', 2001, 4.0)

    def test_correct_init(self):
        self.assertEqual('Bad Boys', self.movie.name)
        self.assertEqual(2000, self.movie.year)
        self.assertEqual(5.0, self.movie.rating)
        self.assertEqual([], self.movie.actors)

    def test_name_empty_string_raises_error(self):
        with self.assertRaises(ValueError) as ex:
            self.movie.name = ''
        self.assertEqual("Name cannot be an empty string!", str(ex.exception))

    def test_incorrect_year_raises_error(self):
        with self.assertRaises(ValueError) as ex:
            self.movie.year = 1700
        self.assertEqual("Year is not valid!", str(ex.exception))

    def test_add_actor_method_name_not_in_the_actor_list(self):
        self.movie.add_actor('Brat Pitt')
        self.assertEqual(['Brat Pitt'], self.movie.actors)

    def test_add_actor_method_name_already_in_the_actor_list(self):
        self.movie.actors = ['Brat Pitt', 'Joro']
        result = self.movie.add_actor('Joro')
        self.assertEqual('Joro is already added in the list of actors!', result)
        self.assertEqual(['Brat Pitt', 'Joro'], self.movie.actors)

    def test_gt_method_our_rating_is_bigger(self):
        result = self.movie.__gt__(self.movie_2)
        self.assertEqual(f'"Bad Boys" is better than "Bad Boys 2"', result)

    def test_gt_method_our_rating_is_lower(self):
        result = self.movie_2.__gt__(self.movie)
        self.assertEqual(f'"Bad Boys" is better than "Bad Boys 2"', result)

    def test_repr_method(self):
        self.movie.actors = ['Brat Pitt', 'Joro']
        expected_result = f"Name: Bad Boys\n" \
                          f"Year of Release: 2000\n" \
                          f"Rating: 5.00\n" \
                          f"Cast: Brat Pitt, Joro"
        result = self.movie.__repr__()
        self.assertEqual(expected_result, result)







if __name__ == '__main__':
    main()