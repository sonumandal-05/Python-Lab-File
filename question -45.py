# 1.The students of Python class are asked to write a program to add 'ing' at the end of a given string
# (length should be at least 3). If the given string already ends with 'ing' then add 'ly' instead. 
# If the string length of the given string is less than 3, leave it unchanged. Can you help them to implement it?  
# Test Case 1 [Input must be a string] 



string = input("Enter a string: ")
if len(string) < 3:
    print(string)
elif string.endswith("ing"):
    print(string + "ly")
else:    print(string + "ing")
