n = int(input("Enter number: "))
r = 1
#ex n = 4

while r <= n:
    c = 1
    al = 65 - r + n
    while c <= r:
        print(chr(al), end=" ")
        al = al + 1
        c = c + 1
    r = r + 1
    print()
