#4.) Invariants ----> Chocolate Problem.
#CODE:

def chocolate_bar(rows, columns):
    total_pieces = rows * columns

    breaks = total_pieces - 1

    return breaks


rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns: "))

print("Minimum number of breaks =", chocolate_bar(rows, columns))