from unittest import TestCase, main

from hash_table import Hashtable


class TestHashTable(TestCase):



  def setUp(self):

    self.table = Hashtable()


  def test_init(self):

    self.assertEqual(4, self.table._Hashtable__max_capacity)

    self.assertEqual([None, None, None, None], self.table._Hashtable__keys)

    self.assertEqual([None, None, None, None], self.table._Hashtable__values)

    self.assertEqual(0, self.table._Hashtable__length)



  def test_add_method_expect_correct_result(self):

    self.table.add('name', 'Peter')

    self.assertEqual('Peter', self.table['name'])



  def test_get_method_return_none_for_not_existing_element(self):

    result = self.table.get('not existing')

    self.assertEqual(None, result)



  def test_get_method_return_message_for_not_existing_element(self):

    result = self.table.get('not existing', 'expected message')

    self.assertEqual('expected message', result)



  def test__getitem__method_correct_data(self):

    self.table['name'] = 'Peter'

    self.assertEqual('Peter', self.table['name'])


  def test__getitem__method_incorrect_key_raises_error(self):

    self.table['name'] = 'Peter'

    with self.assertRaises(KeyError) as ex:

      result = self.table['age']

    self.assertEqual("'age is not in the hash table'", str(ex.exception))


  def test_correct_override(self):

    self.table['name'] = 'Peter'

    self.table['name'] = 'Pesho'

    self.assertEqual('Pesho', self.table['name'])

    self.assertEqual(1, len(self.table))



  def test_resize_correct(self):

    self.table['name'] = 'Peter'

    self.table['age'] = 23

    self.table['three'] = 3

    self.table['blabla'] = True

    self.assertEqual(4, self.table._Hashtable__max_capacity)

    self.table['blabla222'] = False

    self.assertEqual(8, self.table._Hashtable__max_capacity)

    self.assertEqual(5,len(self.table))



  def test_index_creation_on_collision_when_index_is_our_of_range(self):

    self.table['name'] = 'Peter'

    self.table['age'] = 25

    self.table['is_pet_owner'] = True

    result = self.table._Hashtable__calculate_index('is_driver')

    self.assertEqual(0, result)



  def test_str_method(self):

    self.table['name'] = 'Peter'

    self.table['age'] = 35

    expected_result = '{name: Peter, age: 35}'

    result = self.table.__str__()

    self.assertEqual(expected_result, result)



if __name__ == '__main__':

  main()

