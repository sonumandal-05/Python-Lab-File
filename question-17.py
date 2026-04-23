# 7.	Find the maximum of three numbers using if statement only.



num1 = float(input("Please enter the first number: "))
num2 = float(input("Please enter the second number: "))
num3 = float(input("Please enter the third number: "))
if (num1 >= num2) and (num1 >= num3):
    max_num = num1
elif (num2 >= num1) and (num2 >= num3):
    max_num = num2
else:
    max_num = num3
print("The maximum of the three numbers is:", max_num)