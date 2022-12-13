user_input = input("Enter string: ")
len_of_str = int(len(user_input))
f = True
g = True

# To check PALINDROME
for i in range(0,int(len_of_str/2)):
  if user_input[i] != user_input[len_of_str-i-1]:
    print("Not palindrome")
    f = False
    break
if f:
  print("Palindrome")

# To check Symmetric
for i in range(0,int(len_of_str/2)):
  if user_input[i] != user_input[int(len_of_str/2)+i]:
    print("Not symmetric")
    g = False
    break
if g:
  print("Symmetric")
