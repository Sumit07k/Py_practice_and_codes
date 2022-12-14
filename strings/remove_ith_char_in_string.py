user_input = input("Enter string: ")
index_choice = int(input("Enter the index no to remove character: "))
new_string = ''

for i in range(len(user_input)):
  if i != index_choice:
    new_string = new_string + user_input[i]

print("The new string is:  ",new_string)