# 3. Create a dictionary and add key-value pairs in it. Take first input from user, the size of the dictionary and 
# second input as key and third input as the value.  Using for loop iterate over each key-value pair and print the elements of 
# dictionary found during iteration. Test Case: Input: Enter dictionary size: 3 Enter key: 1001 Enter value: Rohit Enter key: 1002
# Enter value: Ram Enter key: 1003 Enter value: Raghav Output: 1001 - Rohit 1002 - Ram 1003 - Raghav 



size = int(input("Enter dictionary size: "))
my_dict = {}
for _ in range(size):
    key = input("Enter key: ")
    value = input("Enter value: ")
    my_dict[key] = value
for key, value in my_dict.items():
    print(f"{key} - {value}")
    