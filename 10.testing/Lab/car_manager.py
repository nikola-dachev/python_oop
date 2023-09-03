from unittest import TestCase, main


class TestCarManager(TestCase):

    def setUp(self):
        self.car = Car('Ford', 'Focus', 5, 50)

    def test_correct_init(self):
        self.assertEqual('Ford', self.car.make)
        self.assertEqual('Focus', self.car.model)
        self.assertEqual(5, self.car.fuel_consumption)
        self.assertEqual(50, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

    def test_incorect_make_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.make = ''
        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_incorrect_model_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.model = ''
        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_incorrect_fuel_consumption_below_zero_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = -1

        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_incorrect_fuel_consumption_equal_zero_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = 0

        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_incorrect_fuel_capacity_below_zero_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = -1
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_incorrect_fuel_capacity_equal_zero_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = 0
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_incorrect_fuel_amount_equal_zero_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = -1
        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_refuel_method_negative_fuel_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(-1)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_refuel_method_zero_fuel_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(0)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_refuel_method_correct_data_for_fuel_successfully_refueled(self):
        self.car.refuel(10)
        self.assertEqual(10, self.car.fuel_amount)

    def test_refuel_method_fuel_more_than_capacity(self):
        self.car.refuel(100)
        self.assertEqual(50, self.car.fuel_amount)

    def test_drive_method_not_enough_fuel_raises_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.drive(100)
        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))

    def test_drive_method_enough_fuel_fuel_amound_decreases(self):
        self.car.fuel_amount = 50
        self.car.drive(100)
        self.assertEqual(45, self.car.fuel_amount)


if __name__ == '__main__':
    main()
