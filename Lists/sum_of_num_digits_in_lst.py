def num_sum(l1):
  l2 = []
  for i in l1:
    ssum = 0
    for j in str(i):
      ssum = ssum + int(j)
    l2.append(ssum)
  print("Sum of digits list: ",l2,end="")

l1 = []
lst_size = int(input("Enter size of list: "))
print("Enter elements")
for i in range(lst_size):
  x = int(input())
  l1.append(x)

print("Original list: ",l1)
num_sum(l1)