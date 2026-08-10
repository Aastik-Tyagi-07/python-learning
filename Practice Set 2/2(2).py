a = int(input("Enter the first number:"))
b = int(input("Enter the second number:"))
operations = input("Enter the operation you want to perform (+, -, *, /):")

match operations:
    case "+":
        print("The addition of a and b =", a+b)
    case "-":
        print("The subtraction of a and b =", a-b)
    case "*":
        print("The multiplication of a and b =", a*b)
    case "/":
        print("The division of a and b =", a/b)
    case _:
        print("Operation not available")
        