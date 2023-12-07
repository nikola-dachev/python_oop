from unittest import TestCase, main
from project.trip import Trip


class TestTrip(TestCase):
  def setUp(self):
    self.non_family_trip = Trip(10000,1, False)
    self.family_trip = Trip(10000, 4, True)

  def test_correct_init(self):
    self.assertEqual(10000, self.non_family_trip.budget)
    self.assertEqual(1, self.non_family_trip.travelers)
    self.assertEqual(False, self.non_family_trip.is_family)
    self.assertEqual({'New Zealand': 7500, 'Australia': 5700, 'Brazil': 6200, 'Bulgaria': 500}, self.family_trip.DESTINATION_PRICES_PER_PERSON)
    self.assertEqual({}, self.family_trip.booked_destinations_paid_amounts)

  def test_invalid_travelers_number_raise(self):
    with self.assertRaises(ValueError) as ex:
      self.non_family_trip.travelers = 0
    self.assertEqual('At least one traveler is required!', str(ex.exception))

  def test_is_family_set_to_false(self):
    self.assertFalse(self.non_family_trip.is_family)

  def test_is_family_set_to_true(self):
    self.assertTrue(self.family_trip.is_family)

  def test_book_a_trip_destination_not_in_destinations(self):
    expected_result = 'This destination is not in our offers, please choose a new one!'
    result = self.family_trip.book_a_trip("Italy")
    self.assertEqual(expected_result, result)

  def test_book_a_trip_for_families(self):
    expected_result = 'Successfully booked destination Bulgaria! Your budget left is 8200.00'
    result = self.family_trip.book_a_trip("Bulgaria")

    self.assertEqual(1800, self.family_trip.booked_destinations_paid_amounts["Bulgaria"])
    self.assertEqual(8200, self.family_trip.budget)
    self.assertEqual(expected_result, result)

  def test_book_a_trip_for_non_family(self):
    result = self.non_family_trip.book_a_trip("Bulgaria")
    expected_result = expected_result = 'Successfully booked destination Bulgaria! Your budget left is 9500.00'

    self.assertEqual(500, self.non_family_trip.booked_destinations_paid_amounts["Bulgaria"])
    self.assertEqual(10000, self.family_trip.budget)
    self.assertEqual(expected_result, result)

  def test_book_a_trip_not_enough_budget(self):
    self.non_family_trip.budget = 10
    result = self.non_family_trip.book_a_trip("Bulgaria")
    expected_result = 'Your budget is not enough!'
    self.assertEqual(expected_result, result)

  def test_booking_status_empty_booked_destinations(self):
    expected_result = 'No bookings yet. Budget: 10000.00'
    result = self.non_family_trip.booking_status()
    self.assertEqual(expected_result, result)

  def test_booking_status_booked_destinations(self):
    self.non_family_trip.book_a_trip("New Zealand")
    self.non_family_trip.book_a_trip("Bulgaria")
    expected_result = 'Booked Destination: Bulgaria\nPaid Amount: 500.00\nBooked Destination: New Zealand\nPaid Amount: 7500.00\nNumber of Travelers: 1\nBudget Left: 2000.00'
    result = self.non_family_trip.booking_status()
    self.assertEqual(expected_result, result)
    self.assertEqual({'New Zealand': 7500.0, 'Bulgaria': 500.0}, self.non_family_trip.booked_destinations_paid_amounts)

if __name__ == "__main__":
  main()