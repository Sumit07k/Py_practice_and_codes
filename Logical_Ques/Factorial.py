number = int(input("Enter number: "))
fact = 1
i = 1

while i != number+1:
    fact = fact * i
    i = i + 1

print("Factorial: ",fact)

#EX = number = 4
"""
1 != 5

fact = 1
i = 2

2 != 5
fact = 2

i = 3
3 != 5
fact = 6

i = 4
4!=5
fact = 24
i = 5


"""