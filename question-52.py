# 8. An English teacher gives a task to students that needs to be done in the following way: the teacher gives a string as input
# then the students need to write the same string in such a way that alphabets in half of the string are in lower case and
# remaining half (later half part) are in upper case. Write a Python program to implement this.


string = input("Enter a string: ")
half_length = len(string) // 2
result = string[:half_length].lower() + string[half_length:].upper()
print("Modified string:", result)
