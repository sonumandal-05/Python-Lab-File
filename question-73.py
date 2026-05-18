# Write a Python program to:
# a)	Store student data in JSON file
# b)	Read and display it



import json
# a) Store student data in JSON file
student_data = {
    "name": "Sonu",
    "age": 18,
    "course": "BCA (AI & ML)"
}
with open('student_data.json', 'w') as file:
    json.dump(student_data, file)
# b) Read and display it
with open('student_data.json', 'r') as file:
    loaded_data = json.load(file)
    print("Student Data:", loaded_data)
    