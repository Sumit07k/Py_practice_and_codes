numb = int(input("Enter number: "))
r = 1
while r <= numb:
    c = 1
    val = r
    while c <= r:
        print(val, end=" ")
        c = c + 1
        val = val - 1
    print()
    r = r + 1
