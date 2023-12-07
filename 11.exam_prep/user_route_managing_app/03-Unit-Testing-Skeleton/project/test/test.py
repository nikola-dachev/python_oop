from project.robot import Robot
from unittest import TestCase, main  

class TestRobot(TestCase):
  def setUp(self):
    self.robot = Robot('R1', 'Military', 5, 500)
    self.robot_2 = Robot('R2', 'Military', 5,600)
    self.robot_3 = Robot('R3', 'Military', 5,400)
    self.robot_4 = Robot('R4', 'Military', 5,400)

  def test_correct_set_up(self):
    self.assertEqual('R1', self.robot.robot_id)
    self.assertEqual('Military', self.robot.category)
    self.assertEqual(5, self.robot.available_capacity)
    self.assertEqual(500,self.robot.price)
    self.assertEqual([], self.robot.hardware_upgrades)
    self.assertEqual([], self.robot.software_updates)

  def test_incorrect_category_raises(self):
    with self.assertRaises(ValueError) as ex:
      self.robot.category = "Bla Bla"
    self.assertEqual("Category should be one of '['Military', 'Education', 'Entertainment', 'Humanoids']'" , str(ex.exception))

  def test_incorrect_price_raises(self):
    with self.assertRaises(ValueError) as ex:
      self.robot.price = -5
    self.assertEqual("Price cannot be negative!", str(ex.exception))

  def test_upgrade_component_in_upgrades(self):
    self.robot.upgrade('CPU', 100)
    expected_result = "Robot R1 was not upgraded."
    result = self.robot.upgrade('CPU', 100)
    self.assertEqual(expected_result, result)

  def test_upgrade_componennt_not_in_upgrades(self):
    result = self.robot.upgrade('CPU', 100)
    expected_result = "Robot R1 was upgraded with CPU."
    self.assertEqual(expected_result, result)
    self.assertEqual(["CPU"], self.robot.hardware_upgrades)
    self.assertEqual(650,self.robot.price)

  def test_update_component_updated(self):
    result = self.robot.update(1, 1)
    expected_result = 'Robot R1 was updated to version 1.'
    self.assertEqual(expected_result, result)
    self.assertEqual([1], self.robot.software_updates)
    self.assertEqual(4, self.robot.available_capacity)
    
  def test_update_component_not_updated_version_less(self):
    self.robot.update(1, 1)
    expected_result = "Robot R1 was not updated."
    result = self.robot.update(1, 1)
    self.assertEqual(expected_result, result)

  def test_update_component_not_updated_not_enough_capacity(self):
    expected_result = "Robot R1 was not updated."
    result = self.robot.update(1, 100000000)
    self.assertEqual(expected_result, result)

  def test_gt_price_lower(self):
    result = self.robot_3.__gt__(self.robot_2)
    expected_result = 'Robot with ID R3 is cheaper than Robot with ID R2.'
    self.assertEqual(expected_result, result)
    
  def test_gt_price_equal(self):
    result = self.robot_3.__gt__(self.robot_4)
    expected_result = 'Robot with ID R3 costs equal to Robot with ID R4.'
    self.assertEqual(expected_result, result)

  def test_gt_price_higher(self):
    result= self.robot_2.__gt__(self.robot_4)
    expected_result = 'Robot with ID R2 is more expensive than Robot with ID R4.'
    self.assertEqual(expected_result, result)

if __name__ == "__main__":
  main()