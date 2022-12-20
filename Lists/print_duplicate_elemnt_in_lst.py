l1 =  [10, 20, 30, 20, 20, 30, 40, 50, -20, 60, 60, -20, -20]
l2 = []
l3 = set(l1)

print(l3)
print("original:",l1)

for i in l3:
  if l1.count(i) > 1:
    l2.append(i)

print(l2)
