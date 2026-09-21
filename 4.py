"""Question 4. Write a python function make_multiplier(facto) that  returns a new function which multiples its
input by factor. [Use fuctions that returns another function that remembers a value.] (Multiple 
greater or closures)."""

#CODE:
def make_multiplier(factor):

    def multiplier(number):
        return number * factor

    return multiplier


double = make_multiplier(2)
triple = make_multiplier(3)

print(double(5))
print(triple(5))