#Implicit & Explicit Type Conversion + invalid Conversion Error

a = 10
b = 5.5

c = a + b

print("Result =", c)
print("Type =", type(c))


x = "100"
y = int(x)

print("Converted value =", y)
print("Type =", type(y))


try:
    value = "Hello"
    number = int(value)

except ValueError:
    print("Error: String cannot be converted to integer")