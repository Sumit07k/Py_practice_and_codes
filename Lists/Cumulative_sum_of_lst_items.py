l1 = [10, 20, 30, 40, 50]
x = len(l1)
l2 = [l1[0]]
print("List 1:",l1)
for i in range(1,x):
  l2.append(l1[i]+l2[i-1])

print("List 2:",l2)