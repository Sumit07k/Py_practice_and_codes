n = int(input("Enter number: "))

rev = 0
# n = 123
while n != 0:
    mod = n % 10
    rev = rev * 10 + mod #321
    n = n // 10
print(rev)
