from project.second_hand_car import SecondHandCar

from unittest import TestCase, main

class TestSecondHandCar(TestCase):
  def setUp(self):
    self.car = SecondHandCar("Toyota", "Corolla", 160000.0, 10000.0)
    self.other_car = SecondHandCar("Opel", "Astra", 260000.0, 1000.0)
    self.other_car_2 = SecondHandCar("Opel", "Astra", 260000.0, 500.0)

  def test_correct_init(self):
    self.assertEqual("Toyota", self.car.model)
    self.assertEqual("Corolla", self.car.car_type)
    self.assertEqual(160000.0, self.car.mileage)
    self.assertEqual(10000.0,self.car.price)
    self.assertEqual([],self.car.repairs)

  def test_incorrect_price_less_than_1_raises(self):
    with self.assertRaises(ValueError) as ex:
      self.car.price = 0.02
    self.assertEqual('Price should be greater than 1.0!', str(ex.exception))

  def test_incorrect_price_equal_to_1_raises(self):
    with self.assertRaises(ValueError) as ex:
      self.car.price = 1.0
    self.assertEqual('Price should be greater than 1.0!', str(ex.exception))

  def test_incorrect_mileage_less_than_100_raises(self):
    with self.assertRaises(ValueError) as ex:
      self.car.mileage = 10
    self.assertEqual('Please, second-hand cars only! Mileage must be greater than 100!',str(ex.exception))

  def test_incorrect_mileage_equal_to_100_raises(self):
    with self.assertRaises(ValueError) as ex:
      self.car.mileage = 100
    self.assertEqual('Please, second-hand cars only! Mileage must be greater than 100!',str(ex.exception))


  def test_set_promotional_price_new_price_greater_than_current_price_raises(self):
    with self.assertRaises(ValueError) as ex:
      self.car.set_promotional_price(20000.0)
    self.assertEqual('You are supposed to decrease the price!', str(ex.exception))

  def test_set_promotional_price_new_price_equal_to_current_price_raises(self):
    with self.assertRaises(ValueError) as ex:
      self.car.set_promotional_price(10000.0)
    self.assertEqual('You are supposed to decrease the price!', str(ex.exception))

  def test_set_promotional_price_new_price_lower_than_current_price(self):
    result = self.car.set_promotional_price(5000.0)
    expected_result = 'The promotional price has been successfully set.'
    self.assertEqual(expected_result, result)
    self.assertEqual(5000.0, self.car.price)

  def test_need_repair_repair_price_greater_than_half_of_current_price_raises(self):
    result = self.car.need_repair(10000.0, 'Repair description')
    expected_result = 'Repair is impossible!'
    self.assertEqual(expected_result, result)

  def test_need_repair_repair_price_lower_than_half_of_current_price(self):
    result = self.car.need_repair(1000.0,'Repair description')
    expected_result = 'Price has been increased due to repair charges.'
    self.assertEqual(expected_result, result)
    self.assertEqual(['Repair description'],self.car.repairs)
    self.assertEqual(11000.0, self.car.price)

  def test_gt_method_different_cars(self):
    result = self.car.__gt__(self.other_car)
    expected_result = 'Cars cannot be compared. Type mismatch!'
    self.assertEqual(expected_result, result)

  def test_gt_method_same_cars(self):
    result = self.other_car.__gt__(self.other_car_2)
    expected_result = True
    self.assertEqual(expected_result, result)

  def test_str_method_no_repairs(self):
    result = self.car.__str__()
    expected_result = """Model Toyota | Type Corolla | Milage 160000.0km
Current price: 10000.00 | Number of Repairs: 0"""
    self.assertEqual(expected_result, result)
    
  def test_str_method_with_repairs(self):
    self.car.need_repair(10000.0, 'Repair description')
    result = self.car.__str__()
    expected_result = """Model Toyota | Type Corolla | Milage 160000.0km
Current price: 10000.00 | Number of Repairs: 0"""
    self.assertEqual(expected_result, result)

if __name__ == "__main__":
  main()
