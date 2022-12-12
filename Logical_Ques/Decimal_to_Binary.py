

num = int(input("Enter number: "))   #user input
ans = 0                # final binary value
i = 0             # iterator used for multiplying by 10
while num != 0:
    mod = num % 2     # to determine the bit value      # mod = num & 1
    ans = mod * pow(10, i) + ans    # to represent in correct binary form
    i += 1     # for power of 10
    num = int(num / 2)   # right shift of num
print(ans, end="")


