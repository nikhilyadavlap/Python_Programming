
#3.) Tumblers Problem
#CODE:

def tumblers(n):
    state = [False] * n

    for i in range(1, n + 1):
        for j in range(i - 1, n, i):
            state[j] = not state[j]

    return state


n = int(input("Enter number of tumblers: "))

result = tumblers(n)

for i in range(n):
    if result[i]:
        print("Tumbler", i + 1, "is ON")


