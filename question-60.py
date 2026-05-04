# • Write a Python program to check whether one set is a subset of another set. 




# Function to check if set1 is a subset of set2
def is_subset(set1, set2):
    return set1.issubset(set2)
# Main function
def main():
    # Create two sets
    set1 = {1, 2, 3}
    set2 = {1, 2, 3, 4, 5}

    # Check if set1 is a subset of set2
    if is_subset(set1, set2):
        print("Set 1 is a subset of Set 2.")
    else:
        print("Set 1 is not a subset of Set 2.")
if __name__ == "__main__":
    main()
    