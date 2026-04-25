# 3. Richa is earning 23rs per month. Her salary gets double in second month and triple in third month and so on.
# Write a python program to print her salary for coming n months individually using while loop.



initial_salary = 23
n = int(input("Enter the number of months: "))  
month = 1
while month <= n:
    if month == 1:
        salary = initial_salary
    elif month == 2:
        salary = initial_salary * 2
    elif month == 3:
        salary = initial_salary * 3
    else:
        salary = initial_salary * month  
    print(f"Month {month}: Salary = {salary} rs")
    month += 1
    