def swap_ele_of_list(l1,x,y):
  l1[x],l1[y] = l1[y],l1[x]
  return l1

len_of_list = int(input("Enter the size of list: "))
l1 = []
for i in range(len_of_list):
  a = int(input("Enter element: "))
  l1.append(a)

x = int(input("Enter the first index of list you want ot interchange: "))
y = int(input("Enter the second index of list you want ot interchange: "))

ans = swap_ele_of_list(l1,x,y)

print(ans)