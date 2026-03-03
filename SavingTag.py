price = float(input("Enter laptop price: "))
savings = float(input("Enter month savings: "))

import math
months_needed = math.ceil(price / savings)

print(months_needed)