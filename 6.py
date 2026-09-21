"""Question 6. Write a decorator logger that prints the arguments a function was called with and
the value it returned."""

#CODE:
def logger(func):

    def wrapper(*args, **kwargs):

        print("Function called with arguments:", args, kwargs)

        result = func(*args, **kwargs)

        print("Returned value:", result)

        return result

    return wrapper


@logger
def add(a, b):
    return a + b


add(10, 20)