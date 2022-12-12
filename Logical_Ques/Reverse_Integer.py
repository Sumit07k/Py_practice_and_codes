n = int(input("Enter number for its reversal: "))     # user input
ans = 0                                             # final reversed value
z = n                                       # copy of original number
n = abs(n)                                          # original value of n without any signs and decimals

while n != 0:                                   #ex = 123 -> 321
    mod = n % 10                        # we get last int
    ans = ans * 10 + mod                    #
    n = n//10                               # floor division

if z > 0:                   # positive, simple print ans
    print(ans)
if z < 0:                   # ex -543
    print(-ans)             # print negative number
