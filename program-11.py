# 1.	Ask the user to input their name and display the length of name excluding spaces.


x = input("Please enter your name: ")
name_length = len(x.replace(" ", ""))
print("The length of your name excluding spaces is:", name_length)