# 	Write a Python program to: 
# a)	Create a user-defined module with functions which Count frequency of characters in a string using dictionary
# b)	Import the module and use its functions in another program 



def count_frequency(input_string):
    frequency = {}
    for char in input_string:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency

if __name__ == "__main__":
    user_input = input("Enter a string: ")
    result = count_frequency(user_input)
    print("Character frequency:", result)
    