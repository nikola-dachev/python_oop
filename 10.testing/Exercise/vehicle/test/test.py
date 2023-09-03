from unittest import TestCase, main

from project.vehicle import Vehicle


class TestVehicle(TestCase):

  def setUp(self):
    self.vehicle = Vehicle(50.0, 109.0)

  def test_init_returns_correct_data(self):
    self.assertEqual(50.0, self.vehicle.fuel)
    self.assertEqual(50.0, self.vehicle.capacity)
    self.assertEqual(109.0, self.vehicle.horse_power)
    self.assertEqual(Vehicle.DEFAULT_FUEL_CONSUMPTION, self.vehicle.fuel_consumption)
    self.assertEqual(1.25,Vehicle.DEFAULT_FUEL_CONSUMPTION)

  def test_drive_method_not_enough_fuel_raises(self):
    with self.assertRaises(Exception) as ex:
      self.vehicle.drive(10000)
    self.assertEqual("Not enough fuel", str(ex.exception))

  def test_drive_method_enough_fuel(self):
    self.assertEqual(50,self.vehicle.fuel)
    self.vehicle.drive(10)
    expected_result = 50 - (10*1.25)
    self.assertEqual(expected_result,self.vehicle.fuel)


  def test_refuel_method_too_much_fuel_raises(self):
    with self.assertRaises(Exception) as ex:
      self.vehicle.refuel(10)
    self.assertEqual("Too much fuel", str(ex.exception))

  def test_refuel_method_not_too_much_fuel(self):
    self.vehicle.fuel = 2
    self.vehicle.refuel(10)
    expected_result = 2 +10
    self.assertEqual(expected_result,self.vehicle.fuel)

  def test_str_method(self):
    expected_result = "The vehicle has 109.0 horse power with 50.0 fuel left and 1.25 fuel consumption"
    self.assertEqual(expected_result,self.vehicle.__str__())

if __name__ =='__main__':
  main()
