numb = int(input("Enter number: "))
r = 1
x = 0
while r <= numb:
    c = 1
    while c <= r:
        print(chr(65 + x), end=" ")
        c = c + 1
    print()
    x = x + 1
    r = r + 1
