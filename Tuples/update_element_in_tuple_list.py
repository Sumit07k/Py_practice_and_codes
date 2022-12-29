l1 = [(1, 3, 4), (2, 4, 6), (3, 8, 1)]
to_be_added = 4

  
for i in range(len(l1)):
  l1[i] = list(l1[i])
  for j in range(len(l1[i])):
    l1[i][j] = l1[i][j] + to_be_added
  l1[i] = tuple(l1[i])


print(l1)