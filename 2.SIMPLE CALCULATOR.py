print("--- SIMPLE CALCULATOR ---")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("\nChoose operation:")
print("+  Addition")
print("-  Subtraction")
print("*  Multiplication")
print("/  Division")

op = input("Enter operation: ")

if op == "+":
    result = num1 + num2
    print("Result =", result)

elif op == "-":
    result = num1 - num2
    print("Result =", result)

elif op == "*":
    result = num1 * num2
    print("Result =", result)

elif op == "/":
    if num2 != 0:
        result = num1 / num2
        print("Result =", result)
    else:
        print("Cannot divide by zero.")

else:
    print("Invalid operation.")