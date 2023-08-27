def read_next(*args):
    for el in args:
        yield ''.join([str(char) for char in el])

for item in read_next("string", (2,), {"d": 1, "i": 2, "c": 3, "t": 4}):
    print(item, end='')

#second option
def read_next(*args):
    for el in args:
        for sub_el in el:
            yield sub_el