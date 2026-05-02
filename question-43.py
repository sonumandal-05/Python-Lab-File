# 3. Richa is earning 23rs per month. Her salary gets double in second month and triple in third month and so on. 
# Write a python program to print her salary for coming n months individually using while loop.




salary = 23
n = int(input("Enter the number of months: "))
print("Richa's salary for each month:")
while n > 0:
    print(salary)
    salary *= (n + 1)  # Double in second month, triple in third month, etc.
    n -= 1
    