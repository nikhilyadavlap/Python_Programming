"""Write a python program to count the no. of vowels, Constants, digits, special characters 
 present in a srting """

text = input("Enter a string: ")

vowels = 0
consonants = 0
digits = 0
special = 0

for ch in text:

    if ch.lower() in "aeiou":
        vowels += 1

    elif ch.isalpha():
        consonants += 1

    elif ch.isdigit():
        digits += 1

    elif not ch.isspace():
        special += 1

print("Vowels =", vowels)
print("Consonants =", consonants)
print("Digits =", digits)
print("Special Characters =", special)