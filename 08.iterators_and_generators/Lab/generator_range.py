def genrange(start, end):
    current_number = start
    while True:
        if current_number <= end:
            yield current_number
            current_number +=1
        else:
            break

print(list(genrange(1, 10)))