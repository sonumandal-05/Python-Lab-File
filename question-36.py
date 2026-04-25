# 6. Jorge is assigned a task to take string input from user and print its individual letters except vowels using while loop in python.
# Note: Use only small letters of alphabets



string = input("Enter a string: ")
index = 0
vowels = 'aeiou'
print("Individual letters except vowels:")
while index < len(string):
    if string[index] not in vowels:
        print(string[index], end=' ')
    index += 1
    