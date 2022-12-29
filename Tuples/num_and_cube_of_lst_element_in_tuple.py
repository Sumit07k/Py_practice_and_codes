# Input: list = [1, 2, 3]
# Output: [(1, 1), (2, 8), (3, 27)]
l1 = []
user_val = int(input("How many values do you want? "))
while user_val !=0:
  l1.append(int(input("Enter val")))
  user_val = user_val - 1
l3 = []
for i in l1:
  l2 = []
  f = pow(i,3)
  l2.append(i)
  l2.append(f)
  l2 = tuple(l2)
  l3.append(l2)
print(l3)

# By list compresion
# ress = [(val,pow(val,3)) for val in [1,2,3,4]]
# print(ress)