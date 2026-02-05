a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
print("Choose the operation (+,-,*,/)")
op = input("Enter operation: ")

match op:
    case "+":
        print("Result:", a + b)
    case "-":
        print("Result:", a - b)
    case "*":
        print("Result:", a * b)
    case "/":
        if b != 0:
            print("Result:", a / b)
        else:
            print("Error: Division by zero")
    case _:
        print("Invalid operator")


