"""Q2. WAP to input the first name, middle and last name of a person. 
Your task is to print the initials of the first and middle name separated by a dot (.)
The last name should be followed by a dot and a space where the first letter is capital. 
Sample Input   Mohandas KaramChand Gandhi 
Sample Output M.K. Gandhi   """

#CODE:
first = input("First Name: ")
middle = input("Middle Name: ")
last = input("Last Name: ")

print(first[0] + "." + middle[0] + ". " + last)