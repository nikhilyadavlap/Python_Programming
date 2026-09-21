"""Question1. Given a list of numbers, use a lambda expression with filter() to keep only
a) even numbers
b) odd numbers
c) prime numbers
d) real numbers
e) rational numbers (p/q)
f) irrational numbers !(p/q)
and a lambda expression to map() to square not of each of them."""

#CODE:

import math
from fractions import Fraction

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", even)

odd = list(filter(lambda x: x % 2 != 0, numbers))
print("Odd numbers:", odd)

prime = list(filter(
    lambda x: x > 1 and all(x % i != 0 for i in range(2, int(math.sqrt(x)) + 1)),
    numbers
))
print("Prime numbers:", prime)

mixed = [2, 3.5, 4 + 2j, -7, 8.2]
real = list(filter(lambda x: isinstance(x, (int, float)), mixed))
print("Real numbers:", real)

mixed2 = [2, Fraction(1, 3), math.sqrt(2), Fraction(5, 2)]
rational = list(filter(lambda x: isinstance(x, (int, Fraction)), mixed2))
print("Rational numbers:", rational)

irrational_values = [math.sqrt(2), math.sqrt(3), math.pi]
irrational = list(filter(lambda x: isinstance(x, float), irrational_values))
print("Irrational numbers:", irrational)

square_roots = list(map(lambda x: math.sqrt(x), numbers))
print("Square roots:", square_roots)