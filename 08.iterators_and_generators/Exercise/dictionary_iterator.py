from typing import Dict


class dictionary_iter:
    def __init__(self,collection: Dict):
        self.items = list(collection.items())
        self.start_index = -1
        self.end_index = len(self.items) - 1

    def __iter__(self):
        return self

    def __next__(self):
        self.start_index +=1
        if self.start_index > self.end_index:
            raise StopIteration

        return self.items[self.start_index]


result = dictionary_iter({"name": "Peter", "age": 24})
for x in result:
    print(x)