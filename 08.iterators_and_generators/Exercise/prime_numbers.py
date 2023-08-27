
#optimal way
from math import sqrt


def get_primes(my_list):
    for number in my_list:
        if number <= 1:
            continue

        for divisor in range(2, int(sqrt(number)) + 1):
            if number % divisor == 0:
                break

        else:
            yield number

print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))


#easier way

# def get_primes(my_list):
#     for number in my_list:
#         if number <= 1:
#             continue
#
#         for divisor in range(2, number):
#             if number % divisor == 0:
#                 break
#
#         else:
#             yield number
#
# print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))