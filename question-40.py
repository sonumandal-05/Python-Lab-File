# 10. Suppose your mom is asking to generate and print a series of numbers up to a given number
# (i.e., number of terms is the input given by her) such that each number in the series is equal to the
# sum of its previous two numbers. Do this problem using Python.
#  Example: 0 1 1 2 3 5 8 13……




n = int(input("Enter the number of terms: "))
a, b = 0, 1
print("Fibonacci series up to", n, ":")
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b
    