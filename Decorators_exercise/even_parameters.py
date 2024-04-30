
def even_parameters(func):
    def wrapper(*args, **kwargs):
        even = all(isinstance(el, int) and el % 2 == 0 for el in args)
        if even:
            return func(*args)

        return 'Please use only even numbers!'

    return wrapper


# other way
# def even_numbers(func):
#     def wrapper(*args, **kwargs):
#         for arg in args:
#             if isinstance(arg, int):
#                 if arg % 2 == 0:
#                     continue
#
#             return 'Please use only even numbers!'
#
#         return func(*args)
#
#     return wrapper


@even_parameters
def add(a, b):
    return a + b


print(add(2, 4))
print(add("Peter", 1))
