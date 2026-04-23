# 8.	Two students want to determine which datatype the provided input belongs to.
# Create a program that prints the class datatype that it belongs to.



user_input = input("Please enter something: ")
input_type = type(user_input)
print(f"The input '{user_input}' belongs to the datatype: {input_type}")
