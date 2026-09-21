#Write a program using a user-defined fuction to check if a given string is a palindrome or not.
#(ignore eases and white spaces)

def check_palindrome(text):
    
    text = text.replace(" ", "").lower()

    if text == text[::-1]:
        return True
    else:
        return False


string = input("Enter a string: ")

if check_palindrome(string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")