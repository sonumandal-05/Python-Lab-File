# • Write a Python program to perform union, intersection, and difference operations on two sets. 



# Function to perform set operations
def set_operations(set1, set2):
    union = set1.union(set2)
    intersection = set1.intersection(set2)
    difference = set1.difference(set2)

    return union, intersection, difference
# Main function
def main():
    # Create two sets
    set1 = {1, 2, 3, 4, 5}
    set2 = {4, 5, 6, 7, 8}

    # Perform set operations
    union, intersection, difference = set_operations(set1, set2)

    # Display the results
    print(f"Set 1: {set1}")
    print(f"Set 2: {set2}")
    print(f"Union: {union}")
    print(f"Intersection: {intersection}")
    print(f"Difference (Set 1 - Set 2): {difference}")
if __name__ == "__main__":
    main()