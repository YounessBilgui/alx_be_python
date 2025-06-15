#accept inputs from user
# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))
# operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()

def perform_operation(num1, num2, operation):
    if "add" in operation:
        return num1 + num2
    elif "subtract" in operation:
        return num1 - num2
    elif "multiply" in operation:
        return num1 * num2
    elif "divide" in operation:
        if num2 == 0:
            return "Cannot divide by zero."
        else:
            return num1 / num2
    else:
        return "Enter a valid operation."
    