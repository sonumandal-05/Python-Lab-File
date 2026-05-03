# 6. Create three dictionaries. For all the three dictionaries, give first input as the size of the dictionary,
# second input as the key and third input as the value. Write a program to concatenate the content of all these three
# dictionariesto create a fourth resultant dictionary.


dict1 = {}
dict2 = {}
dict3 = {}
for i in range(3):
    size = int(input(f"Enter the size of dictionary {i+1}: "))
    for _ in range(size):
        key = input("Enter key: ")
        value = input("Enter value: ")
        if i == 0:
            dict1[key] = value
        elif i == 1:
            dict2[key] = value
        else:
            dict3[key] = value
resultant_dict = {**dict1, **dict2, **dict3}
print("Resultant Dictionary:", resultant_dict)
