numb = int(input("Enter number: "))
r = 1
while r <= numb:
    c = 1
    x = 65
    while c <= numb:
        print(chr(x), end=" ")
        c = c + 1
        x = x + 1
    print()
    r = r + 1
