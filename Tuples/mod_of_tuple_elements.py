t1 = (54,64,77,34,23)
t2 = (4,5,8,2,5)
t3 = []
for i in range(len(t1)):
  t3.append(t1[i]%t2[i])
t3 = tuple(t3)

print("Tuple 1: ",t1)
print("Tuple 2: ",t2)

print("Mod tuple: ",t3)
