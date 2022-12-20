def occur_ls(l1,x):
  count = 0
  for i in l1:
    if i == x:
      count = count + 1
  print("The occurance of ", x , " is " , count)

l1 = [1,2,3,4,6,6,8,3,5,9,9,9,3,6,5,4,5,7,5,4,5,6,2]
print(l1)

x = int(input("Select element of which you want the count of occurance: "))

occur_ls(l1,x)