'''import sys
t1 = (3,5,2,4,75,23,45,7,43,556,23,34,3)
# k = 2
l = []
minn = 0
maxx = 9999999
for i in range(len(t1)):
  if t1[i] > minn:
    minn = t1[i]
  if t1[i] < maxx:
    maxx = t1[i]
l.append(maxx)
l.append(minn)

for i in range(len(t1)):
  if t1[i] < minn and t1[i] not in l:
    minn = t1[i]
  if t1[i] > maxx and t1[i] not in l:
    maxx = t1[i]

l.append(maxx)
l.append(minn)
print(l)
'''

t1 = (324,23,4,3,46,234,36,4,5345,523,5,4323,22)

k = int(input("Enter the value of k: "))

sorted_tuple = sorted(t1)
result_list = []

result_list.append(list(sorted_tuple[:k]))
result_list.append(list(sorted_tuple[-k:]))

print(result_list)