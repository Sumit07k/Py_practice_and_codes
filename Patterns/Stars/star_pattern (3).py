num = int(input("Enter number: "))

r = 1
while r <= num:
    c = 1
    while c <= num:
        if (r - c <= num-1) and (r - c >= 1):
            print(" ", end=" ")
        else:
            print("*", end=" ")
        c = c + 1
    r = r + 1
    print()
