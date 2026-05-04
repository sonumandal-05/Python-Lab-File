# • Write a Python program to create a dictionary of employee names and salaries, then display the employee with the highest salary. 




# Function to find the employee with the highest salary
def find_highest_salary(employee_dict):
    if not employee_dict:
        return None, None

    highest_salary_employee = max(employee_dict, key=employee_dict.get)
    highest_salary = employee_dict[highest_salary_employee]

    return highest_salary_employee, highest_salary
# Main function
def main():
    # Create a dictionary of employee names and salaries
    employees = {
        "Alice": 70000,
        "Bob": 85000,
        "Charlie": 60000,
        "David": 90000,
        "Eve": 75000
    }

    # Find the employee with the highest salary
    employee, salary = find_highest_salary(employees)

    # Display the result
    print(f"Employee with the highest salary: {employee} with a salary of ${salary}")
if __name__ == "__main__":
    main()