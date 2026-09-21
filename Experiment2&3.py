"""Q1. WAP to read the record of n students in a dictionary containing key/value pairs of name: [marks].
 Print the average of the marks obtained by the particular student correct to 2 decimal places. 
Input Format  The first line contains the integer n, the number of student's records. 
The next n lines contain the names and marks obtained by a student, each value separated by a space.
Sample Input  3 
Krishna 67 68 69 
Arjun 70 98 63  
Malika 52 56 60 
Sample Output   56.00  """

#CODE: 

n = int(input())

student_marks = {}

for _ in range(n):
    data = input().split()
    name = data[0]
    marks = list(map(float, data[1:]))
    student_marks[name] = marks

query_name = input()

average = sum(student_marks[query_name]) / len(student_marks[query_name])

print(f"{average:.2f}")