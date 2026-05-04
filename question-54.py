# 10.Write a Python program calculate the sum, by adding all the numbers of a given tuple. 
# Test Case: Input:- Enter the numbers separated by space:12 12 13 Output:- Original Tuple:('12', '12', '13')
# Sum - Adding all the numbers of the said tuple:37 



numbers = input("Enter the numbers separated by space: ").split()
numbers_tuple = tuple(numbers)
print("Original Tuple:", numbers_tuple)
total_sum = sum(int(num) for num in numbers_tuple)
print("Sum - Adding all the numbers of the said tuple:", total_sum)
