#Menu-driven arithmetic program using if-else

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Floor Division")
print("6. Modulus")
print("7. Exponentiation")

choice = int(input("Enter your choice: "))

if choice == 1:
    print("Result =", a + b)

elif choice == 2:
    print("Result =", a - b)

elif choice == 3:
    print("Result =", a * b)

elif choice == 4:
    print("Result =", a / b)

elif choice == 5:
    print("Result =", a // b)

elif choice == 6:
    print("Result =", a % b)

elif choice == 7:
    print("Result =", a ** b)

else:
    print("Invalid choice")