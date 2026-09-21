"""Question 5. Write a decorator times that reads and prints how long the decorated function
code to run, without changing what the fucntion itself computes."""

#CODE:
import time


def timer(func):

    def wrapper():
        start = time.time()

        func()

        end = time.time()

        print("Execution time:", end - start, "seconds")

    return wrapper


@timer
def my_function():
    total = 0

    for i in range(1000000):
        total += i

    print("Sum =", total)


my_function()

