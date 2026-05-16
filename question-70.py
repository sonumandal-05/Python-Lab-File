# Write a Python program to:
# a)	Create a text file
# b)	Write your name and course
# c)	Read and display the content


# a) Create a text file
file_name = "user_info.txt"
# b) Write your name and course
name = input("Enter your name: ")
course = input("Enter your course: ")
with open(file_name, 'w') as file:
    file.write(f"Name: {name}\n")
    file.write(f"Course: {course}\n")
# c) Read and display the content
with open(file_name, 'r') as file:
    content = file.read()
    print("Content of the file:")
    print(content)
    