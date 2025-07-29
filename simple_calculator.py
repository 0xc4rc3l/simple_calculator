# Simple calculator program

def main():
    print("Simple Calculator")
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    operator = input("Enter an operator (+, -, *, /): ")

    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 == 0:
            print("Error: Division by zero is not allowed.")
            return
        result = num1 // num2
    else:
        print("Invalid operator.")
        return

    print("Result:", num1, operator, num2, "=", result)

if __name__ == "__main__":
    main()
