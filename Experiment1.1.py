"""Q2. WAP to read an integer 'n' from STDIN. For all non-negative integers i<n, print i2 on a separate line.  
 Sample input  
 3  
 Sample Output
 1
 2
 4  
 Example  
 The list of non-negative integers that are less than 3 is [0, 1, 2]. The squares of each number is given below:
 0 
 1 
 4  """

#CODE:

n =int(input("Enter number of students: "))

for i in range(n):
    print(i ** 2)