from project.tennis_player import TennisPlayer

from unittest import TestCase, main

class TestTennisPlayer(TestCase):
  def setUp(self):
    self.player =  TennisPlayer(name="Grisho", age=20, points=100.0)
    self.player_2 = TennisPlayer(name="Shisho", age=20, points=10.0)
    self.player_3 = TennisPlayer(name="Chisho", age=20, points=11.0)

  def test_correct_init(self):
    self.assertEqual("Grisho", self.player.name)
    self.assertEqual(20, self.player.age)
    self.assertEqual(100, self.player.points)
    self.assertEqual([], self.player.wins)

  def test_invalid_name_less_than_two_symbols_raises(self):
    with self.assertRaises(ValueError) as ex:
      self.player.name = ""
    self.assertEqual("Name should be more than 2 symbols!", str(ex.exception))

  def test_invalid_name_2_symbols_raises(self):
    with self.assertRaises(ValueError) as ex:
      self.player.name = "as"
    self.assertEqual("Name should be more than 2 symbols!", str(ex.exception))

  def test_invalid_age_less_than_18_raises(self):
    with self.assertRaises(ValueError) as ex:
      self.player.age = 17
    self.assertEqual("Players must be at least 18 years of age!", str(ex.exception))

  def test_add_new_win_tournament_not_in_wins(self):
    self.player.add_new_win("Wimboldone")
    self.assertEqual(["Wimboldone"], self.player.wins)

  def test_add_new_win_tournament_in_wins(self):
    self.player.add_new_win("Wimboldone")
    result = self.player.add_new_win("Wimboldone")
    expected_result = "Wimboldone has been already added to the list of wins!"
    self.assertEqual(["Wimboldone"], self.player.wins)
    self.assertEqual(expected_result, result)

  def test_lt_method_points_bigger_that_the_other(self):
    result = self.player.__lt__(self.player_2)
    expected_result = 'Grisho is a better player than Shisho'
    self.assertEqual(expected_result, result)

  def test_lt_method_points_less_that_the_other(self):
    result = self.player_2.__lt__(self.player)
    expected_result = 'Grisho is a top seeded player and he/she is better than Shisho'
    self.assertEqual(expected_result, result)

  def test_str_method_no_wins(self):
    result = self.player.__str__()
    expected_result = "Tennis Player: Grisho\n" \
     "Age: 20\n" \
     "Points: 100.0\n" \
     "Tournaments won: []"
    self.assertEqual(expected_result, result)

  def test_str_method_two_wins(self):
    self.player.add_new_win("Wimboldone")
    self.player.add_new_win("US Open")
    result = self.player.__str__()
    expected_result = "Tennis Player: Grisho\n" \
     "Age: 20\n" \
     "Points: 100.0\n" \
     "Tournaments won: Wimboldone, US Open"
    self.assertEqual(expected_result, result)