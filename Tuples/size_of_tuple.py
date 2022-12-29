import sys
t1 = (1,2,3,4,5,6,7,8)
print(t1)
print(sys.getsizeof(t1)) # takes garbage values , uses sys library
print(sys.__sizeof__()) #doesn't takes the garbage values
print(len(t1))
