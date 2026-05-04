# • Write a Python program to store marks in a tuple and find the sum and average of all elements. 




# Function to calculate sum and average of marks in a tuple
def calculate_sum_and_average(marks_tuple):
    if not marks_tuple:
        return None, None

    total_sum = sum(marks_tuple)
    average = total_sum / len(marks_tuple)

    return total_sum, average
# Main function
def main():
    # Create a tuple of student marks
    student_marks = (85, 92, 78, 90, 88)

    # Calculate sum and average of marks
    total_sum, average = calculate_sum_and_average(student_marks)

    # Display the results
    print(f"Sum of Marks: {total_sum}")
    print(f"Average Marks: {average:.2f}")
if __name__ == "__main__":
    main()