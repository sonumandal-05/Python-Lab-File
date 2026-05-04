# • Write a Python function to check whether a given string is a palindrome or not. 



# Function to check if a string is a palindrome
def is_palindrome(s):
    # Remove spaces and convert to lowercase
    cleaned_string = s.replace(" ", "").lower()
    
    # Check if the cleaned string is equal to its reverse
    return cleaned_string == cleaned_string[::-1]
# Main function
def main():
    # Input string from the user
    input_string = input("Enter a string: ")

    # Check if the string is a palindrome
    if is_palindrome(input_string):
        print(f'"{input_string}" is a palindrome.')
    else:
        print(f'"{input_string}" is not a palindrome.')
if __name__ == "__main__":
    main()