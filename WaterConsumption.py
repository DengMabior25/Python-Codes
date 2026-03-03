import math
num_people = float(input("Enter number of people: "))
weekly_liters = num_people * 2.5 * 7

gallons_needed = math.ceil(weekly_liters / 19)
total_water_budget = gallons_needed * 19000

print(weekly_liters)
print(gallons_needed)
print(total_water_budget)