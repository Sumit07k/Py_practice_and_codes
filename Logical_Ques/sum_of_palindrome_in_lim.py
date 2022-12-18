# METHOD 1
'''
result = 0
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
for i in range(a,b):
  x = i
  ans = 0
  while i != 0:
    rem = i % 10
    ans = ans * 10 + rem            
    i = i//10
  if ans == x:
    result = result + x

print("Total sum", result)
'''

# METHOD 2
'''
first_num = int(input("Enter first number: "))
second_num = int(input("Enter second number: "))
final_sum = 0


while first_num <= second_num:
  x = str(first_num)  # x contains string type value
  rev = x[::-1] 
  if first_num == int(rev): 
    final_sum = final_sum + first_num
  first_num = first_num + 1

print("Final sum: ",final_sum)
'''