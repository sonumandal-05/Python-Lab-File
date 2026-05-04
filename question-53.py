# 9. Create a dictionary by taking input from the user. Take first input as the no of keyvalue pairs, next inputs as the 
# corresponding key(string type) and value(integer type). Write a program to find out the product of all elements of the dictionary. 




size = int(input("Enter the number of key-value pairs: "))
my_dict = {}
for _ in range(size):
    key = input("Enter key (string type): ")
    value = int(input("Enter value (integer type): "))
    my_dict[key] = value
product = 1
for value in my_dict.values():
    product *= value
print("Product of all elements in the dictionary:", product)
