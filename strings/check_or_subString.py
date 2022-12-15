user_input = input("Enter string: ")
sub_str_to_be_searched = input("Enter the substring you want to search: ")

s = user_input.split()

if sub_str_to_be_searched in s:
  print("Yes")
else:
  print("No")
