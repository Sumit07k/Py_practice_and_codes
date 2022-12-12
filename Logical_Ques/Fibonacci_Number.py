a1 = 0
a2 = 1
a3 = 0
i = 0
num = int(input("Enter the limit: "))
while i != num:
    print(a3, end=" ")            #0 1 2 3 5 8
    a3 = a1 + a2                #
    a1 = a2             # a1 = 1
    a2 = a3            # a2 = 1
    i += 1
