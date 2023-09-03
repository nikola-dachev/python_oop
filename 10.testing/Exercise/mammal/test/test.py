import unittest

from project.mammal import Mammal


class MammalTest(unittest.TestCase):

    def setUp(self):
        self.mammal = Mammal('Sharo', 'dog', 'whof')

    def test_init(self):
        self.assertEqual('Sharo', self.mammal.name)
        self.assertEqual('dog', self.mammal.type)
        self.assertEqual('whof', self.mammal.sound)
        self.assertEqual('animals', self.mammal._Mamal__kingdom)

    def test_make_sound(self):
        expected_result = "Sharo makes whof"
        self.assertEqual(expected_result, self.mammal.make_sound())

    def test_get_kingdom(self):
        self.assertEqual('animals', self.mammal.get_kingdom())

    def test_get_info(self):
        expected_result = "Sharo is of type dog"
        self.assertEqual(expected_result, self.mammal.info())


if __name__ == '__main__':
    unittest.main()
