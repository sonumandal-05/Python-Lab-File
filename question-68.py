# 	Write a Python program to: 
# a)	Pass a list, tuple, and dictionary as arguments to a function 
# b)	Display their elements inside the function 




def display_elements(lst, tpl, dct):
    print("List elements:", lst)
    print("Tuple elements:", tpl)
    print("Dictionary elements:", dct)
my_list = [1, 2, 3]
my_tuple = (4, 5, 6)
my_dict = {'a': 7, 'b': 8, 'c': 9}
display_elements(my_list, my_tuple, my_dict)
