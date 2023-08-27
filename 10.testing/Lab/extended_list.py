class IntegerList:
    def __init__(self, *args):
        self.__data = []
        for x in args:
            if type(x) == int:
                self.__data.append(x)

    def get_data(self):
        return self.__data

    def add(self, element):
        if not type(element) == int:
            raise ValueError("Element is not Integer")
        self.get_data().append(element)
        return self.get_data()

    def remove_index(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        a = self.get_data()[index]
        del self.get_data()[index]
        return a

    def get(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        return self.get_data()[index]

    def insert(self, index, el):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        elif not type(el) == int:
            raise ValueError("Element is not Integer")

        self.get_data().insert(index, el)

    def get_biggest(self):
        a = sorted(self.get_data(), reverse=True)
        return a[0]

    def get_index(self, el):
        return self.get_data().index(el)


import unittest

class IntegerListTest(unittest.TestCase):

    def test_init_all_int(self):
        intiger_inst = IntegerList(1, 2, 3)
        self.assertEqual(3, len(intiger_inst.get_data()))
        self.assertEqual(3, len(intiger_inst._IntegerList__data))

    def test_init_not_all_args_int(self):
        not_intiger_inst = IntegerList('sdfd', False, {}, [], 3.4)

        self.assertEqual(0, len(not_intiger_inst.get_data()))


    def test_get_data_all_int(self):
        intiger_inst = IntegerList(1,2,3)
        self.assertEqual([1,2,3], intiger_inst.get_data())

    def test_add_el_not_int_raises(self):
        intiger_inst = IntegerList(1, 2, 3)
        value = ('sdfd', False, {}, [], 3.4)
        for el in value:
            with self.assertRaises(ValueError) as ex:
                intiger_inst.add(value)
            self.assertEqual("Element is not Integer", str(ex.exception))
        self.assertEqual(3, len(intiger_inst.get_data()))

    def test_add_int(self):
        intiger_inst = IntegerList(1, 2, 3)
        self.assertEqual([1,2,3,4], intiger_inst.add(4))

    def test_remove_index_invalid_index_raises(self):
        intiger_inst = IntegerList(1, 2, 3)
        with self.assertRaises(IndexError) as ex:
            intiger_inst.remove_index(10)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_remove_index_valid_index(self):
        intiger_inst = IntegerList(1, 2, 3)
        self.assertEqual(3, len(intiger_inst.get_data()))
        result = intiger_inst.remove_index(0)
        self.assertEqual(2, len(intiger_inst.get_data()))
        self.assertEqual(1,result)
        self.assertEqual([2,3],intiger_inst.get_data())

    def test_get_index_invalid_index_raises(self):
        intiger_inst = IntegerList(1, 2, 3)
        with self.assertRaises(IndexError) as ex:
            intiger_inst.get(10)
        self.asserEqual("Index is out of range", str(ex.exception))

    def test_get_index_valid_index(self):
        intiger_inst = IntegerList(1, 2, 3)
        self.assertEqual(3, len(intiger_inst.get_data()))
        self.assertEqual(1, intiger_inst.get(0))
        self.assertEqual(3, len(intiger_inst.get_data()))

    def test_insert_method_invalid_index_raises(self):
        intiger_inst = IntegerList(1, 2, 3)
        with self.assertRaises(IndexError) as ex:
            intiger_inst.insert(10,100)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_insert_method_invalid_type_raises(self):
        intiger_inst = IntegerList(1, 2, 3)
        values = (3.3, 'abf', False, {}, [])
        for el in values:
            with self.assertRaises(ValueError) as ex:
                intiger_inst.insert(0,el)
            self.assertEqual("Element is not Integer", str(ex.exception))

    def test_insert_method_valid_index_and_type(self):
        intiger_inst = IntegerList(1, 2, 3)
        self.assertEqual([1,2,3], intiger_inst.get_data())
        self.assertEqual(3, len(intiger_inst.get_data()))
        result = intiger_inst.insert(0, 10)
        self.assertEqual([10,1,2,3], intiger_inst.get_data())
        self.assertEqual(4, len(intiger_inst.get_data()))

    def test_biggest_method(self):
        intiger_inst = IntegerList(1, 2, 3)
        self.assertEqual(3, intiger_inst.get_biggest())

    def test_get_index_method(self):
        intiger_inst = IntegerList(1, 2, 3)
        self.assertEqual(0, intiger_inst.get_index(1))

if __name__ == '__main__':
    unittest.main()