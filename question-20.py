# 10.	Nishant wants his younger sister, Ruhi to learn the python program for logical operators so 
# he asks her to perform the program by taking the input value in terms of true and false, and print the results
# for and, or, and not operator. Write a python program to help Ruhi in writing the code.


a = input("Enter first value True/False: ")
b = input("Enter second value True/False: ")

a = True if a == "True" else False
b = True if b == "True" else False

print("a and b =", a and b)
print("a or b  =", a or b)
print("not a   =", not a)
print("not b   =", not b)