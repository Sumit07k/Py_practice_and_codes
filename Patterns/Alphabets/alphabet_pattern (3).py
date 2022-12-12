numb = int(input("Enter number: "))
r = 1
while r <= numb:
    c = 1

    while c <= numb:
        print(chr(65 + r + c - 2), end=" ")
        c = c + 1

    print()
    r = r + 1
