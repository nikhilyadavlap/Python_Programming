"""Write a python program to reverse a string with and without slicing also check if the string is an
Anagram. """

text = input("Enter a string: ")

reverse = text[::-1]

print("Reversed string:", reverse)

text = input("Enter a string: ")

reverse = ""

for ch in text:
    reverse = ch + reverse

print("Reversed string:", reverse)

str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

str1 = str1.replace(" ", "").lower()
str2 = str2.replace(" ", "").lower()

if sorted(str1) == sorted(str2):
    print("Strings are anagrams")
else:
    print("Strings are not anagrams")