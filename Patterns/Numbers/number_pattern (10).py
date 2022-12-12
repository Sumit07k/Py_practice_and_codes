n = int(input("Enter no: "))

row = 1
while row <= n:
    col = 1
    spaces = n - row
    count = 1
    while spaces:
        print(" ", end=" ")
        spaces = spaces - 1
        col = col + 1
    while col <= n:
        print(count, end=" ")
        col = col + 1
        count = count + 1
    x = row - 1
    while x:
        print(x, end=" ")
        x = x - 1
    row = row + 1
    print()
