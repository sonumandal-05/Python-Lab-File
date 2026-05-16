# Write a Python program to:
# a)	Store a dictionary using pickle
# b)	Retrieve and display it


import pickle
# a) Store a dictionary using pickle
my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}
with open('my_dict.pkl', 'wb') as file:
    pickle.dump(my_dict, file)
# b) Retrieve and display it
with open('my_dict.pkl', 'rb') as file:
    loaded_dict = pickle.load(file)
    print("Retrieved dictionary:", loaded_dict)
    