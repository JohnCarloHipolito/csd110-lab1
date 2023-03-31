def takeInput():
    first_num = int(input("1st number: "))
    second_num = int(input("2nd number: "))
    operator = input("Operator(+,-,*,/): ")
    return operator, first_num, second_num

def displayResult(operator, first_num, second_num):
    if operator == '+':
        print(first_num, operator, second_num, "=", first_num + second_num)
    elif operator == '-':
        print(first_num, operator, second_num, "=", first_num - second_num)
    elif operator == '*':
        print(first_num, operator, second_num, "=", first_num * second_num)
    elif operator == '/':
        print(first_num, operator, second_num, "=", first_num / second_num)
    else:
        print("Error!!! Incorrect operator.", operator)

#MAIN PROGRAM FLOW
(operator, first_num, second_num) = takeInput()
displayResult(operator, first_num, second_num)