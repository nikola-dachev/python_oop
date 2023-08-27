class sequence_repeat:
    def __init__(self, sequence: str, number: int):
        self.sequence = sequence
        self.number = number
        self.start_index = -1
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.start_index +=1
        self.counter += 1

        if self.counter > self.number:
            raise StopIteration

        if self.start_index > len(self.sequence) - 1:
            self.start_index = 0

        return self.sequence[self.start_index]


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')