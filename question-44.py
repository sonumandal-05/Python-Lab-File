# 4. Humpty Sharma believes in the relationship between numbers.
# He decides to go ahead for his Dulhania with the permission of parents. 
# He will call parents from number who’s sum of digits is
# greater than 60 by calculating the sum of the digits.
# Write a python program to implement the logic.


x = int(input("Enter a number: "))
digit_sum = sum(int(digit) for digit in str(x))
if digit_sum > 60:
    print(f"The sum of digits of {x} is {digit_sum}, which is greater than 60. Humpty can call the parents.")
else:
    print(f"The sum of digits of {x} is {digit_sum}, which is not greater than 60. Humpty cannot call the parents.")
    