n = int(input("Enter number up to which you want to enter: "))
i = 1
while i <= n:
    if i % 2 != 0:
        print(i, end=" ")
    i = i + 1
