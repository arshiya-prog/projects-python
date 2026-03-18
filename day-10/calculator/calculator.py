# from logo import logo

# print(logo)

wants_to_continue = 0

def calc(num1, num2, operation):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        result = num1 / num2

    return result

while wants_to_continue == 0 or wants_to_continue == 1:
    if wants_to_continue == 0:
        num1 = float(input("What's the first number? "))

    print("+\n-\n*\n/")
    operation = input("Pick an operation: ")
    num2 = float(input("What's the second number? "))

    result = calc(num1, num2, operation)
    print(result)

    same_number_continue = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")

    if same_number_continue == 'y':
        wants_to_continue = 1
        num1 = result
    elif same_number_continue == 'n':
        wants_to_continue = 0