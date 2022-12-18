def list_sum(l1):
  total = 0
  for i in l1:
    total = total + i
  return total

l1 = []
x = int(input("Enter no of list elements you want to enter: "))

for i in range(x):
  a = int(input("Enter element "))
  l1.append(a)

res = list_sum(l1)

print("The sum of list elements is: ", res)
