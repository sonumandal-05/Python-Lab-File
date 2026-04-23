# Q1. There are two friend “A” and “B”. They find some apples in a forest. Given the number of
# apples as input, type “yes” if they can be distributed among the two of them, else print “no”.



apples = int(input("Enter the number of apples: "))
if apples % 2 == 0:
    print("Yes, the apples can be distributed among A and B.")