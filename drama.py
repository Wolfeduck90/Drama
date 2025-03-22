# Get input from the user
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))
operator = input("Enter an operator (+, -, *, /): ")

# Perform the calculation based on the operator
if operator == "+":
    result = number1 + number2
elif operator == "-":
    result = number1 - number2
elif operator == "*":
    result = number1 * number2
elif operator == "/":
    if number2 != 0:  # Prevent division by zero
        result = number1 / number2
    else:
        result = "Error: Division by zero is not allowed."
else:
    result = "Invalid operator entered."

# Display the result
print("Result:", result)
