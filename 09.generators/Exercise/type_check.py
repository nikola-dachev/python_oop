def type_check(expected_type):
    def decorator(function):
        def wrapper(*args):
            for arg in args:
                if not isinstance(arg, expected_type):
                    return 'Bad Type'
            result = function(*args)
            return result
        return wrapper
    return decorator

@type_check(int)
def times2(num):
    return num*2

print(times2(2))
print(times2('Not A Number'))