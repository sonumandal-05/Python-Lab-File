# • Write a Python program to remove duplicate elements from a list and sort the remaining elements in ascending order. 


# Function to remove duplicates and sort the list
def remove_duplicates_and_sort(input_list):
    # Remove duplicates by converting the list to a set, then back to a list
    unique_elements = list(set(input_list))
    
    # Sort the list in ascending order
    unique_elements.sort()
    
    return unique_elements
# Main function
def main():
    # Create a list with duplicate elements
    original_list = [5, 3, 8, 1, 2, 5, 3, 7]

    # Remove duplicates and sort the list
    result = remove_duplicates_and_sort(original_list)

    # Display the results
    print(f"Original List: {original_list}")
    print(f"List after removing duplicates and sorting: {result}")
if __name__ == "__main__":
    main()
    