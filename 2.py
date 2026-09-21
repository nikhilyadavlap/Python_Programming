"""Question 2. Write a python program to compute GCD(Greatest common divisor) and LCM of two numbers. Use the 
Euclidean Algorithm of Recursion."""

#CODE:

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def lcm(a, b):
    return abs(a * b) // gcd(a, b)


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("GCD =", gcd(a, b))
print("LCM =", lcm(a, b))