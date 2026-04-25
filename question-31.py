# 1. A professor writes every number with a secret code on a board (where he is multiplying every digit of the number)
# as given below in the sample patterns. He wants to automate the process using Python. Can you help him? 
# Sample pattern:
# 235 = 30
# 150 = 0
# 151 = 5


number = input("Enter a number: ")
product = 1
for digit in number:
    product *= int(digit)
print(f"The product of the digits in {number} is: {product}")

