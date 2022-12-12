n = int(input("Enter no: "))

row = 1
while row <= n:
    col = 1
    spaces = n - row
    while spaces:
        print(" ", end=" ")
        spaces = spaces - 1
        col = col + 1
    while col <= n:
        print(row, end=" ")
        col = col + 1
    row = row + 1
    print()
