# 2. Soham is playing a game of numbers where Soham is counting till an input number less than 98.
# Each time when Soham encounters a multiple of five, he just passes (keep mum) instead of a number.
# Write a program for implementing the same.



n = int(input("Enter a number less than 98: "))
print("Soham's counting:")
for i in range(1, n + 1):
    if i % 5 == 0:
        print("Pass", end=" ")
    else:
        print(i, end=" ")
        