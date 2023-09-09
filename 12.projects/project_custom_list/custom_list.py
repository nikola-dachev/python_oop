class CustomList:
    def __init__(self, *args):
        self.__list = list(args)

    def __is_index_valid(self, index):
        if not isinstance(index, int):
            raise ValueError('Index should be an integer')

        if 0 <= index < len(self.__list):
            return True
        return False

    def append(self, value):
        self.__list.append(value)
        return self.__list

    def remove(self, index):
        if not self.__is_index_valid(index):
            raise ValueError('Index out of range')

        item = self.__list.pop(index)
        return item

    def get(self, index):
        if not self.__is_index_valid(index):
            raise ValueError('Index out of range')
        return self.__list[index]

    def extend(self, values):
        self.__list.extend(values)
        return self.__list

    def insert(self, index, value):
        if not self.__is_index_valid(index):
            raise ValueError('Index out of range')

        self.__list.insert(index, value)
        return self.__list

    def pop(self):
        if len(self.__list) == 0:
            raise ValueError('List is empty')
        element = self.__list.pop(-1)
        return element

    def clear(self):
        self.__list = []

    def index(self, value):
        if value not in self.__list:
            raise ValueError('Value is not in the list')

        return self.__list.index(value)

    def count(self, value):
        return self.__list.count(value)

    def reverse(self):
        return self.__list[::-1]

    def copy(self):
        return self.__list.copy()

    def size(self):
        return len(self.__list)

    def add_first(self, value):
        self.__list.insert(0, value)

    def dictionize(self):
        my_dict = {}

        for index in range(0, len(self.__list), 2):
            key = self.__list[index]

            try:
                value = self.__list[index + 1]

            except IndexError:
                value = ' '

            my_dict[key] = value

        return my_dict

    def move(self, n):
        if not isinstance(n, int):
            raise ValueError(f'{n} is not an integer')

        if n >= len(self.__list):
            raise ValueError('Nothing to move')

        first_part = self.__list[:n]
        second_part = self.__list[n:]
        self.__list = second_part + first_part
        return self.__list

    def return_len_or_el(self, el):
        try:
            return len(el)

        except TypeError:
            return el

    def sum(self):
        result = 0

        for el in self.__list:
            result += self.return_len_or_el(el)
        return result

    def overbound(self):
        max_num = float('-inf')
        biggest_index = 0

        for index in range(len(self.__list)):
            current_num = self.return_len_or_el(self.__list[index])

            if current_num > max_num:
                max_num = current_num
                biggest_index = index
        return biggest_index

    def underbound(self):
        min_num = float('inf')
        smallest_index = 0

        for index in range(len(self.__list)):
            current_num = self.return_len_or_el(self.__list[index])

            if current_num < min_num:
                min_num = current_num
                smallest_index = index
        return smallest_index


# cl = CustomList(122, 2, 311, 'sdddd', 'dddddddddddddd')
#
# print(cl.underbound())
