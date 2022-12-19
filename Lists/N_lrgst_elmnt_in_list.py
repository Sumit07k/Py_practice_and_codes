def N_largest(l1,x): # ex = 3
  l2 = []
  l1.sort(reverse=True)
  for i in range(x):
    l2.append(l1[i])
  return str(l2)

l1 = []
x = int(input("Enter no of list elements you want to enter: "))

for i in range(x):
  a = int(input("Enter element "))
  l1.append(a)

no_of_el = int(input("Enter no of largest element you want: "))

res = N_largest(l1,no_of_el)

print(res)
