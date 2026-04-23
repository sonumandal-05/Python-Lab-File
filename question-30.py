# Q10. Rohit purchased the ball pens from three shops for the coming term end examination
# (TEE). He purchased x pens from the first shop, y pens from the second shop and is yet to buy
# pens from the third shop. Rohit is very superstitious and believes that if the sum of pens he
# buys from the three shops is a divisible by 5, he'll clear the TEE. Please help him by calculating
# for him the minimum number of pens that if purchased from the third shop will make the sum
# of pens as divisible 5.
# print(p_shop3)




x = int(input("Enter the number of pens bought from the first shop: "))
y = int(input("Enter the number of pens bought from the second shop: "))
total_pens = x + y
remainder = total_pens % 5
if remainder == 0:
    print("Rohit can buy 0 pens from the third shop to make the total divisible by 5.")
else:
    pens_needed = 5 - remainder
    print(f"Rohit needs to buy {pens_needed} pens from the third shop to make the total divisible by 5.")
    