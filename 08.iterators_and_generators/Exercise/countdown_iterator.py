class countdown_iterator:
    def __init__(self, count):
        self.count = count
        self.current_count = self.count +1
        self.my_list = []

    def __iter__(self):
        return self

    def __next__(self):
        self.current_count -= 1

        if self.current_count < 0:
            raise StopIteration
        return self.current_count



iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")