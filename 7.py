"""Question 7. Write a generator function fibonacci_generator (n) that yields the first n 
fibonacci numbers one at a time."""

#CODE:
def fibonacci_generator(n):

    a = 0
    b = 1

    for i in range(n):

        yield a

        a, b = b, a + b


n = int(input("Enter n: "))

for number in fibonacci_generator(n):
    print(number)