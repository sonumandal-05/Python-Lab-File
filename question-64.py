# • Write a Python function to calculate the sum of digits of a given number.




# Function to calculate the sum of digits of a given number
def sum_of_digits(n):
    # Convert the number to a string to iterate through each digit
    digits = str(n)
    
    # Calculate the sum of digits
    total_sum = sum(int(digit) for digit in digits)
    
    return total_sum
# Main function
def main():
    # Input number from the user
    number = int(input("Enter a number: "))

    # Calculate the sum of digits
    result = sum_of_digits(number)

    # Display the result
    print(f"The sum of digits of {number} is: {result}")
if __name__ == "__main__":
    main()