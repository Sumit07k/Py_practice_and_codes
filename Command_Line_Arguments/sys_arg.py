import sys

n = len(sys.argv)
print("Total arguments passed:", n)

print("Name of python script: ",sys.argv[0])

print("total arguments\n")
for i in range(1, n):
	print(sys.argv[i], end=" ")
