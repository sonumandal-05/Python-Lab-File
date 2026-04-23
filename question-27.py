# Q7. To reduce the pollution, the Delhi government has decided to apply the odd-even system
# by this winter in the state. In this system, vehicles with odd numbers will be allowed to operate
# in MWFS (Monday, Wednesday, Friday, and Sunday) and vehicles with even numbers will be
# allowed in TTS (Tuesday, Thursday and Saturday) in a week. Can you help the Delhi
# government to implement this system in Python?





vehicle_number = input("Enter the vehicle number: ")
if vehicle_number[-1].isdigit():
    last_digit = int(vehicle_number[-1])
    if last_digit % 2 == 0:
        print("The vehicle with number", vehicle_number, "is allowed to operate on TTS (Tuesday, Thursday, Saturday).")
    else:
        print("The vehicle with number", vehicle_number, "is allowed to operate on MWFS (Monday, Wednesday, Friday, Sunday).")
else:
    print("Invalid vehicle number. Please enter a valid vehicle number ending with a digit.")
    