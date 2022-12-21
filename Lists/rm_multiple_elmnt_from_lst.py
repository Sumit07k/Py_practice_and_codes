def rm_multiple(l1,l2):
  l3 = []
  l3.extend(l1)
  for i in l1:
    if i in l2:
      l3.remove(i)
  return l3

lst_size = int(input("Enter no of elements for the list: "))
l1 = []
l2 = []
for i in range(lst_size):
  x = int(input("Enter element:"))
  l1.append(x)

rm_lst_size = int(input("Enter no of elements you want to remove: "))
for j in range(rm_lst_size):
  y = int(input("Enter element: "))
  l2.append(y)

result = rm_multiple(l1,l2)

print("List after removing elements: ",result,end="")