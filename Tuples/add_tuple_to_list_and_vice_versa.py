l1 = [1,2,3,4]
t1 = (5,6,7,8)
l2 = [9,10,11,12]
t2 = (13,14,15,16)

print("List 1:",l1)
print("Tuple 1:",t1)
print("List added to tuple:")
t1 = tuple(list(t1)+l1)
print(t1,type(t1))

print("List 1:",l2)
print("Tuple 1:",t2)
print("Tuple added to list:")
l2.extend(list(t2))
print(l2, type(l2))