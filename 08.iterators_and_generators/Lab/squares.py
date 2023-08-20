def squares(n):
    counter = 1
    while True:
        if counter<= n:
            yield counter ** 2
            counter += 1
        else:
            break

print(list(squares(5)))