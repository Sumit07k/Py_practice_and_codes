x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number: "))

n = int(input("ENter the number to which the permutation sum should not equal to: "))

new_lst =[[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i + j + k != n]

print(new_lst)