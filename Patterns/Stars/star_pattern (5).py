numb = int(input("Enter number: "))
r = 1
while r <= numb:
    c = 1
    while c <= r:
        print("*", end=" ")
        c = c + 1
    print()
    r = r + 1
