#    Write a program to: 
# •	Use a lambda function to find square of numbers in a list 
# •	Use assert statement to ensure input list is not empty 



numbers = [1, 2, 3, 4, 5]
assert len(numbers) > 0, "Input list cannot be empty"
squared_numbers = list(map(lambda x: x ** 2, numbers))
print("Squared numbers:", squared_numbers)
