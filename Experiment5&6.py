"""Q1. Using functions, re-write and execute Python program to:
1.Add natural numbers upto n where n is taken as an input from user.
2.Print Fibonacci series till nth term (Take input from user).  """

#CODE:
def add(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

n = int(input("Enter number: "))
print((n))
print(add(n))