from unittest import TestCase, main

from project.railway_station import RailwayStation
from collections import deque


class TestRailwayStation(TestCase):
    def setUp(self):
        self.railway = RailwayStation("Sofia")

    def test_correct_init(self):
        self.assertEqual("Sofia", self.railway.name)
        self.assertEqual(deque([]),self.railway.arrival_trains)
        self.assertEqual(deque([]),self.railway.departure_trains)

    def test_len_name_less_than_3_symbols_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.railway.name = "ab"
        self.assertEqual("Name should be more than 3 symbols!", str(ex.exception))

    def test_len_name_3_symbols_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.railway.name = "abc"
        self.assertEqual("Name should be more than 3 symbols!", str(ex.exception))

    def test_len_name_0_symbols_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.railway.name = ""
        self.assertEqual("Name should be more than 3 symbols!", str(ex.exception))

    def test_new_arival(self):
        self.railway.new_arrival_on_board("Varna - Sofia")
        self.assertEqual(deque(["Varna - Sofia"]),self.railway.arrival_trains)

    def test_train_has_arrived_different_arrival_trains_raises(self):
        self.railway.new_arrival_on_board("Varna - Sofia")
        result = self.railway.train_has_arrived("Burgas - Sofia")
        expected_result = "There are other trains to arrive before Burgas - Sofia."
        self.assertEqual(expected_result, result)


    def test_train_has_arrived(self):
        self.railway.new_arrival_on_board("Varna - Sofia")
        result = self.railway.train_has_arrived("Varna - Sofia")
        expected_result = "Varna - Sofia is on the platform and will leave in 5 minutes."
        self.assertEqual(expected_result, result)
        self.assertEqual(deque(["Varna - Sofia"]),self.railway.departure_trains)

    def test_train_has_arrived_more_than_one_arrived_trains(self):
        self.railway.new_arrival_on_board("Varna - Sofia")
        self.railway.new_arrival_on_board("Burgas - Sofia")
        result = self.railway.train_has_arrived("Varna - Sofia")
        expected_result = "Varna - Sofia is on the platform and will leave in 5 minutes."
        self.assertEqual(expected_result, result)
        self.assertEqual(deque(["Varna - Sofia"]),self.railway.departure_trains)

    def test_train_has_left_return_true(self):
        self.railway.new_arrival_on_board("Varna - Sofia")
        self.railway.train_has_arrived("Varna - Sofia")
        result = self.railway.train_has_left("Varna - Sofia")
        self.assertEqual(True,result)
        self.assertEqual(deque([]), self.railway.departure_trains)

    def test_traiin_has_not_left_yet_raises(self):
        self.railway.new_arrival_on_board("Varna - Sofia")
        self.railway.train_has_arrived("Varna - Sofia")
        result = self.railway.train_has_left("Burgas - Sofia")
        self.assertEqual(False, result)
        self.assertEqual(deque(["Varna - Sofia"]), self.railway.departure_trains)

if __name__ == "__main__":
    main()