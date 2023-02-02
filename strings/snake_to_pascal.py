test = "hello_my_name_is_sumit"
new = test.split("_")
res=[]
for i in new:
  i = i.title()
  res.append(i)

res = "".join(res)
print("New string:",res)