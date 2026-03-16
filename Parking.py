vehicle = input("Enter vehicle type (motorcycle, car, bus): ")
hours = int(input("Enter number of hours parked: "))

first_hour_rate = 0
additional_rate = 0

if vehicle == "motorcycle":
    first_hour_rate, additional_rate = 1, 0.5
elif vehicle == "car":
    first_hour_rate, additional_rate = 2, 1
elif vehicle == "bus":
    first_hour_rate, additional_rate = 3, 2
else:
    print("Invalid vehicle type.")
    exit()

if hours <= 1:
    total_fee = first_hour_rate
else:
    total_fee = first_hour_rate + (hours - 1) * additional_rate

print(total_fee)
