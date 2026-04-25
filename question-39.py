# 9.Perfect number is a positive number which sum of all positive divisors excluding that number is equal to that number.
# For example, 6 is perfect number since divisor of 6 are 1, 2 and 3. Sum of its divisor is 1 + 2+ 3 = 6.
# Write a python program to print perfect number series up to N, where N is entered by user.



n = int(input("Enter a number: "))
print(f"Perfect numbers up to {n}:")
for num in range(1, n + 1):
    divisor_sum = sum(i for i in range(1, num) if num % i == 0)
    if divisor_sum == num:
        print(num)
        