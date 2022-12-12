n = int(input("Enter no: "))
twice_n = 2*n-1

row = 0
while row < twice_n:
    col = 0
    while col < twice_n:
        m = min(row, col)
        m = min(m, twice_n-row-1)
        m = min(m, twice_n-col-1)
        print(n-m, end=" ")
        col = col + 1
    row = row + 1
    print()
