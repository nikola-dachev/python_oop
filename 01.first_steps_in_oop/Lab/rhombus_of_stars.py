n = int(input())

def print_figure(n, count):
    print(' ' * (n - count), end='')
    print(*['*'] * count)

def print_triangle(n):
    for count in range(1, n + 1):
        print_figure(n, count)

def print_reverse_triangle(n):
    for count in range(n-1,0,-1):
        print_figure(n, count)


print_triangle(n)
print_reverse_triangle(n)