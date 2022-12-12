numb = int(input("Enter number: "))
r = 1
x = 64
while r <= numb:
    c = 1
    x = x + 1
    while c <= numb:
        print(chr(x), end=" ")
        c = c + 1
        # x = x + 1
    print()
    r = r + 1
