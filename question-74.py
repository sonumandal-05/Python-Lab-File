# Write a Python program to handle:
# a)	Division by zero
# b)	Invalid input



# a) Division by zero
try:
    numerator = float(input("Enter the numerator: "))
    denominator = float(input("Enter the denominator: "))
    result = numerator / denominator
    print(f"Result: {result}")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
# b) Invalid input
try:
    number = int(input("Enter an integer: "))
    print(f"You entered: {number}")
except ValueError:
    print("Error: Invalid input. Please enter an integer.")
    