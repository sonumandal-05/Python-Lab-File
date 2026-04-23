# 9.	If a five-digit even number is an input through the keyboard,
# write a program to calculate the sum of its digits.




number = input("Please enter a five-digit even number: ")
if len(number) == 5 and number.isdigit() and int(number) % 2 == 0:
    digit_sum = sum(int(digit) for digit in number)
    print(f"The sum of the digits in the number {number} is: {digit_sum}")
else:
    print("Invalid input. Please enter a five-digit even number.")
    