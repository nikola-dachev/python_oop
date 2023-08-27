class Cat:
    def __init__(self, name):
        self.name = name
        self.fed = False
        self.sleepy = False
        self.size = 0

    def eat(self):
        if self.fed:
            raise Exception('Already fed.')
        self.fed = True
        self.sleepy = True
        self.size += 1

    def sleep(self):
        if not self.fed:
            raise Exception('Cannot sleep while hungry')
        self.sleepy = False


import unittest


class CatTests(unittest.TestCase):
    def test_initialize_cat(self):
        cat = Cat('Sharo')

        self.assertEqual('Sharo', cat.name)
        self.assertEqual(False, cat.fed)
        self.assertEqual(False, cat.sleepy)
        self.assertEqual(0, cat.size)

    def test_cat_eats(self):
        cat = Cat('Sharo')
        self.assertEqual(False, cat.fed)

        cat.eat()
        self.assertEqual(True, cat.fed)
        self.assertEqual(True, cat.sleepy)
        self.assertEqual(1, cat.size)

        with self.assertRaises(Exception) as ex:
            cat.eat()

        self.assertEqual('Already fed.', ex.exception.args[0])

    def test_cat_hungry_cannot_fall_asleep(self):
        cat = Cat('Sharo')
        self.assertEqual(False, cat.fed)

        with self.assertRaises(Exception) as ex:
            cat.sleep()
        self.assertEqual('Cannot sleep while hungry', ex.exception.args[0])

    def test_cat_is_fed_can_fall_asleep(self):
        cat = Cat('Sharo')
        cat.eat()
        self.assertEqual(True, cat.fed)

        cat.sleep()
        self.assertEqual(False, cat.sleepy)


if __name__ == '__main__':
    unittest.main()