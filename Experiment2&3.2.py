"""Q3. Rupal has a huge collection of country stamps. 
She decided to count the total number of distinct country stamps in her collection. 
She asked for your help. You pick the stamps one by one from a stack of country stamps. 
Find the total number of distinct country stamps using a suitable data type. 
Note: Apply your knowledge of the .add() operation from set to help your friend Rupal.  """

#CODE:
n = int(input())

stamps = set()

for i in range(n):
    country = input()
    stamps.add(country)

print(len(stamps))