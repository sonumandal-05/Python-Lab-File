# Q3. Write a program to take the sides of a triangle as input and determine whether it is an
# equilateral, isosceles or scalene triangle.


side1 = float(input("Enter the length of the first side of the triangle: "))
side2 = float(input("Enter the length of the second side of the triangle: "))
side3 = float(input("Enter the length of the third side of the triangle: "))
if side1 == side2 == side3:
    print("The triangle is an equilateral triangle.")
elif side1 == side2 or side2 == side3 or side1 == side3:
    print("The triangle is an isosceles triangle.")
else:
    print("The triangle is a scalene triangle.")
    