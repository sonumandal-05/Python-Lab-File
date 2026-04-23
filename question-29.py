# Q9. You are a teacher assigning grades to students based on their exam scores. Implement a
# program that takes a student's score as input and prints their corresponding grade. If the score
# is 90 or above, the grade is 'A'. If the score is between 80 and 89, the grade is 'B'. If the score
# is between 70 and 79, the grade is 'C'. If the score is below 70, the grade is 'F'.



score = float(input("Enter the student's score: "))
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
else:
    grade = 'F'
print(f"The student's grade is: {grade}")