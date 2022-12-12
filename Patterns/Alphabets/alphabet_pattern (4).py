numb = int(input("Enter number: "))
r = 1
x = 0
while r <= numb:
    c = 1
    while c <= numb:
        print(chr(65 + x), end=" ")
        c = c + 1
        x = x + 1
    print()
    r = r + 1
