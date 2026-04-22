# 4.	Ask the user to input their name and any character.
# Display the length of name excluding spaces and count of character (case sensitive) in name.


x = input("Please enter your name: ")
character = input("Please enter a character to count in your name: ")
name_length = len(x.replace(" ", ""))
character_count = x.count(character)
print("The length of your name excluding spaces is:", name_length)
print(f"The count of character '{character}' in your name is:", character_count)
