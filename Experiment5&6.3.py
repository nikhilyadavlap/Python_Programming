"""Q3. Write a Python program to find the maximum and minimum values in a given list of tuples using lambda function.  
Original list with tuples:  
[('V', 62), ('VI', 68), ('VII', 72), ('VIII', 70), ('IX', 74), ('X', 65)]  
Output-  
Maximum and minimum values of the said list of tuples: (74, 62)  """

#CODE:
data = [('V', 62), ('VI', 68), ('VII', 72), ('VIII', 70), ('IX', 74), ('X', 65)]

maximum = max(data, key=lambda x: x[1])
minimum = min(data, key=lambda x: x[1])

print("Maximum: ", maximum)
print("Minimum: ", minimum)
