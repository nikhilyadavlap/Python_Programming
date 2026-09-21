"""Q3. WAP to read an integer from STDIN. Without using any string methods, print the following on a single line:
  123…n  
  Note that … represents the consecutive values in between. 
  Example n=5  
  Output- 12345  """

#CODE:
n = int(input())

for i in range(1, n + 1):
    print(i, end="")