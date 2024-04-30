def type_check(expected_type):
    def decorator(func):
        def wrapper(*args, **kwargs):
            return func(*args) if all(isinstance(arg, expected_type) for arg in args) else 'Bad Type'

        return wrapper

    return decorator


@type_check(int)
def times2(num):
    return num*2


print(times2(2))
print(times2('Not A Number'))
