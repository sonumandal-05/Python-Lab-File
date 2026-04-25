# 7. Strong number is a special number whose sum of the factorial of digits is equal to the original number. 
# For Example: 145 is strong number. Since, 1! + 4! + 5! = 145.
# Write a python program to print all strong number series between the range entered by the user.





x = int(input("Enter the starting number: "))
y = int(input("Enter the ending number: "))
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
print(f"Strong numbers between {x} and {y}:")
for num in range(x, y + 1):
    sum_of_factorials = sum(factorial(int(digit)) for digit in str(num))
    if sum_of_factorials == num:
        print(num)
        