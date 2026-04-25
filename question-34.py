# 4. Humpty Sharma believes in the relationship between numbers. He decides to go ahead for his Dulhania with 
# the permission of parents. He will call parents from number who’s sum of digits is greater than 60 by calculating the 
# sum of the digits. Write a python program to implement the logic.




number = input("Enter a number: ")
digit_sum = sum(int(digit) for digit in number)
if digit_sum > 60:
    print("You can call your parents.")
else:
    print("You cannot call your parents.")
    