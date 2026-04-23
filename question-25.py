# Q5. A man has purchased three eatable items like Pizza, Burger, and Pasta at the cost of Rs. X,
# Rs. Y, Rs. Z. He has paid the bill. He wants to check the largest and the lowest cost
# mathematically. Design a code to check the item with the largest price for him.



X = float(input("Enter the cost of Pizza: "))
Y = float(input("Enter the cost of Burger: "))
Z = float(input("Enter the cost of Pasta: "))
largest_cost = max(X, Y, Z)
lowest_cost = min(X, Y, Z)
print("The largest cost is:", largest_cost)
print("The lowest cost is:", lowest_cost)

