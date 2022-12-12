num1 = int(input("Enter first number: "))
operation_choice = int(input("Enter choice\n1.Add\n2.Subtract\n3.Multiply\n4.Divide\n"))
num2 = int(input("Enter second number: "))
result = 0
if operation_choice == 1:
    result = num1 + num2
elif operation_choice == 2:
    result = num1 - num2
elif operation_choice == 3:
    result = num1 * num2
elif operation_choice == 4:
    result = num1 / num2
print("The answer is: ", result)
repeat_choice = input("Want to repeat again - y/n: ")
result_second = result
if repeat_choice == 'y':
    while 1:
        num3 = int(input("Enter number: "))
        operation_choice = int(input("Enter choice\n1.Add\n2.Subtract\n3.Multiply\n4.Divide"))
        if operation_choice == 1:
            result_second = result_second + num3
        elif operation_choice == 2:
            result_second = result_second - num3
        elif operation_choice == 3:
            result_second = result_second * num3
        elif operation_choice == 4:
            result_second = result_second / num3
        print("Final answer: ", result_second)
        repeat_choice = input("Want to repeat again - y/n: ")
        if repeat_choice == 'y':
            continue
        else:
            exit()
