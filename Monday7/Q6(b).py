#Hexadecimal -> Decimal Binary and Octal

hex_num = input("Enter a hexadecimal number: ")

decimal = int(hex_num, 16)

print("Decimal =", decimal)
print("Binary =", bin(decimal))
print("Octal =", oct(decimal))