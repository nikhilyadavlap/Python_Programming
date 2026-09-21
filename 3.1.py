#2.) Bridge Problem
#CODE:

def bridge_problem(times):
    times.sort()
    total_time = 0

    while len(times) > 3:
        a = times[0]
        b = times[1]
        y = times[-2]
        z = times[-1]

        method1 = a + 2 * b + z
        method2 = 2 * a + y + z

        total_time += min(method1, method2)

        times.pop()
        times.pop()

    if len(times) == 3:
        total_time += sum(times)

    elif len(times) == 2:
        total_time += times[1]

    elif len(times) == 1:
        total_time += times[0]

    return total_time


people = [1, 2, 5, 10]

print("Minimum time =", bridge_problem(people))

