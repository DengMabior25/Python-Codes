import math
length = float(input("Enter room length: "))
width = float(input("Enter room width: "))
height = float(input("Enter room height: "))

wall_area = 2 * (length + width) * height
cans_needed = math.ceil(wall_area / 10)

print(wall_area)
print(cans_needed)