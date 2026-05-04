# 7. Create a dictionary by taking input from the user. Take first input as the no. of keyvalue pairs and next inputs as the values
# of key-value pair. Check if it is empty or not. If it is empty then display the message “ Empty” otherwise dispay the
# content of the dictionary. 



size = int(input("Enter the number of key-value pairs: "))
my_dict = {}
for _ in range(size):
    key = input("Enter key: ")
    value = input("Enter value: ")
    my_dict[key] = value
if not my_dict:
    print("Empty")
else:
    print("Dictionary content:", my_dict)
    