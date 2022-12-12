numb = int(input("Enter number: "))
r = 1
count = 1
while r <= numb:
    c = 1
    while c <= r:
        print(count, end=" ")
        c = c + 1
        count = count + 1
    print()
    r = r + 1
