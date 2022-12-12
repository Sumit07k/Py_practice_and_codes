num = int(input("Enter number: "))

row = 1

while row <= num:
    col = 1
    while col <= num:
        if row + col <= num:      # will print spaces
            print(" ", end=" ")
        else:                      # will print stars
            print("*", end=" ")
        col = col + 1
    row = row + 1
    print()
