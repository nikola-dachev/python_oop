class Worker:
    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')
        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f'{self.name} has saved {self.money} money.'



import unittest


class WorkerTests(unittest.TestCase):
    def test_worker_created_correctly(self):
        worker = Worker('Pesho', 2000, 100)
        self.assertEqual('Pesho', worker.name)
        self.assertEqual(2000, worker.salary)
        self.assertEqual(100, worker.energy)
        self.assertEqual(0, worker.money)

    def test_worker_works(self):
        worker = Worker('Pesho', 2000, 100)
        worker.work()

        expected_money = 2000
        expected_energy = 100 - 1
        self.assertEqual(expected_money, worker.money)
        self.assertEqual(expected_energy, worker.energy)

        worker.work()
        expected_money = 2000 + 2000
        expected_energy = 100 - 1 - 1
        self.assertEqual(expected_money, worker.money)
        self.assertEqual(expected_energy, worker.energy)

    def test_worker_has_not_enough_energy(self):
        worker = Worker('Pesho', 2000, 0)

        with self.assertRaises(Exception) as ex:
            worker.work()
        self.assertEqual('Not enough energy.', ex.exception.args[0])

        worker = Worker('Pesho', 2000, -1)
        with self.assertRaises(Exception) as ex:
            worker.work()

        self.assertEqual('Not enough energy.', ex.exception.args[0])

    def test_worker_rested(self):
        worker = Worker('Pesho', 2000, 100)
        self.assertEqual(100, worker.energy)

        worker.rest()
        expected_energy = 100 + 1
        self.assertEqual(expected_energy, worker.energy)

        worker.rest()
        expected_energy = 100 + 1 + 1
        self.assertEqual(expected_energy, worker.energy)

    def test_worker_get_info_method(self):
        worker = Worker('Pesho', 2000, 100)

        result = worker.get_info()
        expected_result = "Pesho has saved 0 money."
        self.assertEqual(expected_result, result)

        worker.work()
        result = worker.get_info()
        expected_result = "Pesho has saved 2000 money."
        self.assertEqual(expected_result, result)


if __name__ == '__main__':
    unittest.main()
