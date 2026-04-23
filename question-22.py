# Q2. Given a parameter "X". Show the output as an area of a circle if the choice is the letter "c"
# or the area of the square if the choice is "s". Round off to 2 decimal places.


choice=input("Enter 'c' for area of circle or 's' for area of square: ")
choice=choice.lower()
X=float(input("Enter the value of X: "))
if choice == 'c':
    area_circle = 3.14 * X**2
    print("Area of the circle is:", round(area_circle, 2))
elif choice == 's':
    area_square = X**2
    print("Area of the square is:", round(area_square, 2))
else:
    print("Invalid choice. Please enter 'c' or 's'.")