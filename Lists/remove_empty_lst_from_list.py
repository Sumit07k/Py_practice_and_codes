def rm_empty_lst(l1):
  for i in l1:
    if i == []:
      l1.remove(i)
  print(l1)

l1 = [4,7,5,2,5,[],85,[],44,3,6,[],6]

rm_empty_lst(l1)
