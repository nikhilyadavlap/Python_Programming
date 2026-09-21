"""Q1. Using functions, re-write and execute Python program to:
1.Add natural numbers upto n where n is taken as an input from user.
2.Print Fibonacci series till nth term (Take input from user).  """

#CODE:
def fibonacci(n):
    a = 0
    b = 1

    for i in range(n):
        print(a, end=" ")
        c = a + b
        a = b
        b = c

n = int(input("Enter number of terms: "))
fibonacci(n)