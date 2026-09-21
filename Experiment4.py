"""Q1.  WAP to enter a string and a substring. 
You have to print the number of times that the substring occurs in the given string. 
String traversal will take place from left to right, not from right to left.
Sample Input  ABCDCDC CDC 
Sample Output  2  """

#CODE:
string = input()
substring = input()

count = 0

for i in range(len(string)):
    if string[i:i+len(substring)] == substring:
        count += 1

print(count)