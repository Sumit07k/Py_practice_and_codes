n = int(input("Enter number: "))
sums = 0
x = n

while n != 0:
    mod = n % 10
    sums = sums + mod*mod*mod
    n = n//10

if sums == x:
    print("Armstrong number")
else:
    print("Not Armstrong")
# 1 + 125 + 27 = 153
