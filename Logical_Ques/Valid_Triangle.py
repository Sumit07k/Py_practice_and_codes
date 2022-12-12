print("Enter sides: ")
a = int(input("First side: "))
b = int(input("second side: "))
c = int(input("third side: "))

if a + b > c:
    if b + c > a:
        if a + c > b:
            print("Valid triangle")
        else:
            print("Not Valid")
    else:
        print("Not Valid")
else:
    print("not Valid")
