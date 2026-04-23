# Q4. Write a python program to determine the price of the gym membership with GST of 5%
# on the net amount based on the following table

# Month        Charges (per month)
# Range
#                   2000/pm
# 1-2 
#                    1500/pm

# 3-9
#                      1000/pm
                     
# 10-12
#                       800/pm  
# >12


months = int(input("Enter the number of months for gym membership: "))
if 1 <= months <= 2:
    price_per_month = 2000
elif 3 <= months <= 9:
    price_per_month = 1500
elif 10 <= months <= 12:
    price_per_month = 1000
else:
    price_per_month = 800
net_amount = price_per_month * months
gst = net_amount * 0.05
total_amount = net_amount + gst
print(f"The total price of the gym membership for {months} months is: {total_amount:.2f}")
