class reverse_iter:
    def __init__(self, collection):
        self.collection = collection
        self.start_index = 0
        self.end_index = len(collection) - 1
        self.current_index = len(collection)

    def __iter__(self):
        return self

    def __next__(self):
        self.current_index -=1
        if self.current_index < self.start_index:
            raise StopIteration

        return self.collection[self.current_index]

reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)
