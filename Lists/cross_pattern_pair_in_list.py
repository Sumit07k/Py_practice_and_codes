l1 = [1,2,3,4]
l2 = [5,6,7,8]
l3 = []
for i in range(0,len(l1),2):
  l3.append((l1[i],l2[i+1]))
  
  l3.append((l1[i+1],l2[i]))

print(l3)