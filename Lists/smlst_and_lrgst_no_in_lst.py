def lst_smallst_num(l1):
  l1.sort()
  return l1[0]

def lst_lrgst_num(l1):
  l1.sort()
  return l1[-1]

l1 = []
x = int(input("Enter no of list elements you want to enter: "))

for i in range(x):
  a = int(input("Enter element "))
  l1.append(a)

choice = int(input("You want smallest or largest? 1.Smallest 2.Largest"))

if choice == 1:
  res1 = lst_smallst_num(l1)
  print(res1)

if choice == 2:
  res2 = lst_lrgst_num(l1)
  print(res2)