from unittest import TestCase, main

from custom_list import CustomList


class TestCustomList(TestCase):

    def setUp(self):
        self.custom_list = CustomList(1, 2, 3)

    def test_append_method(self):
        self.custom_list.append(4)
        self.assertEqual([1, 2, 3, 4], self.custom_list._CustomList__list)
        self.assertEqual(4, self.custom_list.size())

    def test_remove_index_is_valid(self):
        result = self.custom_list.remove(0)
        self.assertEqual(1, result)
        self.assertEqual([2, 3], self.custom_list._CustomList__list)

    def test_remove_index_not_valid_index_float_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.custom_list.remove(2.5)
        self.assertEqual('Index should be an integer', str(ex.exception))

    def test_get_index(self):
        result = self.custom_list.get(0)
        self.assertEqual(1, result)
        self.assertEqual([1, 2, 3], self.custom_list._CustomList__list)

    def test_extend(self):
        result = self.custom_list.extend([1, 2])
        self.assertEqual([1, 2, 3, 1, 2], result)
        self.assertEqual([1, 2, 3, 1, 2], self.custom_list._CustomList__list)

    def test_insert_method_invalid_index(self):
        with self.assertRaises(ValueError) as ex:
            self.custom_list.insert(100, 3)
        self.assertEqual('Index out of range', str(ex.exception))

    def test_insert_method(self):
        result = self.custom_list.insert(0, 30)
        self.assertEqual([30, 1, 2, 3], self.custom_list._CustomList__list)
        self.assertEqual([30, 1, 2, 3], result)

    def test_pop_list_is_empty_raises_error(self):
        cl = CustomList()
        self.assertEqual(0, len(cl._CustomList__list))
        with self.assertRaises(ValueError) as ex:
            cl.pop()
        self.assertEqual('List is empty', str(ex.exception))

    def test_pop(self):
        result = self.custom_list.pop()
        self.assertEqual(3, result)
        self.assertEqual([1, 2], self.custom_list._CustomList__list)

    def test_clear(self):
        self.custom_list.clear()
        self.assertEqual([], self.custom_list._CustomList__list)

    def test_index_not_valid_value_raises(self):
        with self.assertRaises(ValueError) as ex:
            self.custom_list.index(400)
        self.assertEqual('Value is not in the list', str(ex.exception))

    def test_index_method_value_correct(self):
        result = self.custom_list.index(1)
        self.assertEqual(0, result)

    def test_count(self):
        result = self.custom_list.count(3)
        self.assertEqual(1, result)

    def test_reverse(self):
        custom_list_id = id(self.custom_list._CustomList__list)
        result = self.custom_list.reverse()
        id_reversed_list = id(result)
        self.assertEqual([3, 2, 1], result)
        self.assertNotEqual(custom_list_id, id_reversed_list)

    def test_copy(self):
        custom_list_id = id(self.custom_list._CustomList__list)
        result = self.custom_list.copy()
        id_copy_list = id(result)
        self.assertEqual([1, 2, 3], result)
        self.assertNotEqual(custom_list_id, id_copy_list)

    def test_size_method(self):
        self.assertEqual(3, len(self.custom_list._CustomList__list))
        result = self.custom_list.size()
        self.assertEqual(3,result)

    def test_add_first(self):
        self.assertEqual([1, 2, 3], self.custom_list._CustomList__list)
        self.custom_list.add_first(5)
        self.assertEqual([5, 1, 2, 3], self.custom_list._CustomList__list)

    def test_dictionize(self):
        self.assertEqual([1, 2, 3], self.custom_list._CustomList__list)
        result = self.custom_list.dictionize()
        self.assertEqual({1: 2, 3: " "}, result)
        self.assertEqual([1, 2, 3], self.custom_list._CustomList__list)

    def test_dictionize_with_even_key_values(self):
        cl = CustomList(1, 2, 3, 4)
        result = cl.dictionize()
        self.assertEqual({1: 2, 3: 4}, result)

    def test_move_method_n_not_int(self):
        with self.assertRaises(ValueError) as ex:
            self.custom_list.move(2.5)
        self.assertEqual('2.5 is not an integer', str(ex.exception))

    def test_number_of_moves_bigger_than_the_len(self):
        with self.assertRaises(ValueError) as ex:
            self.custom_list.move(100)
        self.assertEqual('Nothing to move', str(ex.exception))

    def test_move_method(self):
        self.assertEqual([1, 2, 3], self.custom_list._CustomList__list)
        self.custom_list.move(2)
        self.assertEqual([3, 1, 2], self.custom_list._CustomList__list)

    def test_sum(self):
        cl = CustomList(1, 2, 3, [1, 2], 4, 'asd')
        result = cl.sum()
        self.assertEqual(15, result)

    def test_overbound(self):
        cl = CustomList(1, 2, 3, 4, [1, 2], 'asd')
        self.assertEqual([1, 2, 3, 4, [1, 2], 'asd'], cl._CustomList__list)
        self.assertEqual(4,cl._CustomList__list[3])
        result = cl.overbound()
        self.assertEqual(3,result)

    def test_underbound_element_is_smalles(self):
        cl = CustomList(1, 2, 3, [1, 2], 4, 'asd')
        self.assertEqual([1, 2, 3, [1, 2], 4, 'asd'], cl._CustomList__list)
        self.assertEqual(1,cl._CustomList__list[0])
        result = cl.underbound()
        self.assertEqual(0,result)

    def test_underbound_len_is_smallest(self):
        cl = CustomList(11, 22, 33, [1, 2], 4, 'asd')
        self.assertEqual([11, 22, 33, [1, 2], 4, 'asd'], cl._CustomList__list)
        self.assertEqual([1, 2], cl._CustomList__list[3])
        result = cl.underbound()
        self.assertEqual(3, result)


if __name__ == '__main__':
    main()


