n = int(input("Enter number of elements: "))
l1 = []
for i in range(n):
    print("Enter element no ", i+1)
    l1.append(input())

s = ''

l1.sort()

z = len(l1[0])

i = 0
while i < z and l1[0][i] == l1[z-1][i]:
    i = i + 1
s = l1[0][:i]
print(s)
