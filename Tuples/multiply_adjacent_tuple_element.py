t1 = (1, 5, 7, 8, 10)
t1 = list(t1)
for i in range(0,len(t1)-1):
  t1[i] = t1[i]*t1[i+1]
del t1[-1]
t1 = tuple(t1)

print(t1)