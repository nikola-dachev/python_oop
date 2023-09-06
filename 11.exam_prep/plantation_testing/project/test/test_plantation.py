from project.plantation import Plantation
from unittest import TestCase, main


class TestPlantation(TestCase):
    def setUp(self):
        self.plantation = Plantation(3)

    def test_correct_init(self):
        self.assertEqual(3, self.plantation.size)
        self.assertEqual({}, self.plantation.plants)
        self.assertEqual([], self.plantation.workers)

    def test_size_negative_value_raises_error(self):
        with self.assertRaises(ValueError) as ex:
            self.plantation.size = -1

        self.assertEqual("Size must be positive number!", str(ex.exception))

    def test_hire_worker_method_worker_already_in_the_list(self):
        self.plantation.workers = ['Joro', 'Pesho']

        with self.assertRaises(ValueError) as ex:
            self.plantation.hire_worker('Joro')
        self.assertEqual("Worker already hired!", str(ex.exception))
        self.assertEqual(['Joro', 'Pesho'], self.plantation.workers)

    def test_hire_worker_method_worker_not_in_the_list(self):
        self.assertEqual([], self.plantation.workers)
        result = self.plantation.hire_worker('Joro')
        self.assertEqual(['Joro'], self.plantation.workers)
        self.assertEqual("Joro successfully hired.", result)

    def test_len_method(self):
        self.plantation.plants = {'Joro': ['daisy'], 'Pesho': ['rose']}
        result = self.plantation.__len__()
        self.assertEqual(2, result)

    def test_planting_method_worker_not_in_the_list_raises_error(self):
        with self.assertRaises(ValueError) as ex:
            self.plantation.planting('Joro', 'violet')
        self.assertEqual("Worker with name Joro is not hired!", str(ex.exception))

    def test_planting_method_worker_in_plant_dict(self):
        self.plantation.hire_worker('Joro')
        self.plantation.plants = {'Joro': ['daisy'], 'Pesho': ['rose']}
        self.assertEqual({'Joro': ['daisy'], 'Pesho': ['rose']}, self.plantation.plants)
        result = self.plantation.planting('Joro', 'violet')
        self.assertEqual({'Joro': ['daisy', 'violet'], 'Pesho': ['rose']}, self.plantation.plants)
        self.assertEqual("Joro planted violet.", result)

    def test_planting_method_worker_not_in_plant_dict(self):
        self.plantation.hire_worker('Joro')
        self.plantation.plants = {'Pesho': ['rose']}
        self.assertEqual({'Pesho': ['rose']}, self.plantation.plants)
        result = self.plantation.planting('Joro', 'daisy')
        self.assertEqual({'Pesho': ['rose'], 'Joro': ['daisy']}, self.plantation.plants)
        self.assertEqual("Joro planted it's first daisy.", result)

    def test_planting_method_len_bigger_than_size(self):
        self.plantation.size = 0
        self.plantation.workers = ['Joro']
        with self.assertRaises(ValueError) as ex:
            self.plantation.planting('Joro', 'violet')
        self.assertEqual("The plantation is full!", str(ex.exception))

    def test_str(self):
        self.plantation.workers = ['Joro', 'Pesho']
        self.plantation.plants = {'Joro': ['daisy'], 'Pesho': ['rose', 'violet']}

        result = self.plantation.__str__()
        expected_result = "Plantation size: 3\n" + \
                          "Joro, Pesho\n" + \
                          "Joro planted: daisy\n" + \
                          "Pesho planted: rose, violet"
        self.assertEqual(expected_result, result)

    def test_repr(self):
        self.plantation.workers = ['Joro', 'Pesho']
        result = self.plantation.__repr__()
        expected_result = "Size: 3\n" + \
                          "Workers: Joro, Pesho"
        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    main()
