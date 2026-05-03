# 4. Write a Python program calculate the product, multiplying all the numbers of a given tuple. Test Case Input Enter the numbers
# seperated by space:12 12 output Original Tuple:('12', '12') Product - multiplying all the numbers of the said tuple: 144 



numbers = input("Enter the numbers separated by space: ").split()
numbers_tuple = tuple(numbers)
print("Original Tuple:", numbers_tuple)
product = 1
for num in numbers_tuple:
    product *= int(num)
print("Product - multiplying all the numbers of the said tuple:", product)
