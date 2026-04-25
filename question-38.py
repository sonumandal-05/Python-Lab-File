# 8. If the sum of nth power (where n is the number of digits in the input number) of each digit is equal to the original number
# then the number is known as Armstrong number. For example if the number is 153 then its Armstrong 
# number will be (1*1*1)+(5*5*5)+(3*3*3) = 153. Write a program to check weather a entered number is Armstrong number or not.
# Note: use for loop to solve the problem.



number = int(input("Enter a number: "))
num_str = str(number)
num_digits = len(num_str)
armstrong_sum = sum(int(digit) ** num_digits for digit in num_str)
if armstrong_sum == number:
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")