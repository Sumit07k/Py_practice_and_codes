up_to_range = int(input("Enter number: "))

for i in range(2, up_to_range+1):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i, end=" ")

