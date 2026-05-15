#	Write a Python program to: 
# a)	Define a function to calculate factorial 
# b)	Call the function and display the result 


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
number = int(input("Enter a number: "))
result = factorial(number)
print("The factorial of", number, "is:", result)
