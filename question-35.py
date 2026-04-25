# 5. Rovin just hates the character 'y'. He copies all in his speech character by character until the hate character 'y' 
# is encountered. Design a program to output all the characters in the string until 'y' is encountered.


input_string = input("Enter a string: ")
result = ""
for char in input_string:
    if char.lower() == 'y':
        break
    result += char
print("Output until 'y' is encountered:", result)
