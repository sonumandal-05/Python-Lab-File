# Q6. An electronics store has the following rates for different types of laptop brands:
#  1. Acer – 25000
#  2. Hp – 35000
#  3. Dell – 45000
#  4. Asus – 60000
#  5. Apple – 80000
# They are giving a 10% discount for online booking and 8% discount for advance booking and
# no discount is given for on-spot booking.
#  1. First user input will be booking types like online, advance, or window booking.
#  2. Second user input will be brand.
#  3. Compute and print the amount.



booking_type = input("Enter the booking type (online, advance, or window): ").lower()
brand = input("Enter the laptop brand (Acer, Hp, Dell, Asus, Apple ): ").lower()
if brand == "acer":
    price = 25000
elif brand == "hp":
    price = 35000
elif brand == "dell":
    price = 45000
elif brand == "asus":
    price = 60000
elif brand == "apple":
    price = 80000
else:
    print("Invalid brand entered.")
    price = 0
if booking_type == "online":
    discount = 0.10
elif booking_type == "advance":
    discount = 0.08
elif booking_type == "window":
    discount = 0.0
else:
    print("Invalid booking type entered.")
    discount = 0.0
final_price = price * (1 - discount)
print(f"The final price of the laptop is: {final_price:.2f}")

    
    
