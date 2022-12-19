def even(l1):
  l2 = []
  for i in range(len(l1)):
    if l1[i] % 2 == 0:
      l2.append(l1[i])
  return l2

def odd(l1):
  l2 = []
  for i in range(len(l1)):
    if l1[i] % 2 != 0:
      l2.append(l1[i])
  return l2


l1 = []
x = int(input("Enter no of list elements you want to enter: "))

for i in range(x):
  a = int(input("Enter element "))
  l1.append(a)

choice = int(input("You want even or odd? 1.even 2.odd"))

if choice == 1:
  res1 = even(l1)
  print(res1)

if choice == 2:
  res2 = odd(l1)
  print(res2)
