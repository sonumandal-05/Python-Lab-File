# • Write a Python program to convert a tuple into a list, modify it, and convert it back into a tuple. 




# Function to convert tuple to list, modify it, and convert back to tuple
def modify_tuple(input_tuple):
    # Convert tuple to list
    temp_list = list(input_tuple)
    
    # Modify the list (for example, add an element)
    temp_list.append("new_element")
    
    # Convert back to tuple
    modified_tuple = tuple(temp_list)
    
    return modified_tuple
# Main function
def main():
    # Create a tuple
    original_tuple = (1, 2, 3, 4)

    # Modify the tuple
    modified_tuple = modify_tuple(original_tuple)

    # Display the results
    print(f"Original Tuple: {original_tuple}")
    print(f"Modified Tuple: {modified_tuple}")
if __name__ == "__main__":
    main()