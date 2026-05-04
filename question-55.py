# • Write a Python program to create a list of student marks and display the highest, lowest, and average marks. 



# Function to calculate highest, lowest, and average marks
def calculate_marks(marks):
    if not marks:
        return None, None, None

    highest = max(marks)
    lowest = min(marks)
    average = sum(marks) / len(marks)

    return highest, lowest, average
# Main function
def main():
    # Create a list of student marks
    student_marks = [85, 92, 78, 90, 88]

    # Calculate highest, lowest, and average marks
    highest, lowest, average = calculate_marks(student_marks)

    # Display the results
    print(f"Highest Marks: {highest}")
    print(f"Lowest Marks: {lowest}")
    print(f"Average Marks: {average:.2f}")
if __name__ == "__main__":
    main()
    