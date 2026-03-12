hours = int(input("Enter number of hours parked: "))
if hours <= 2:
    fee = 5000
else:
    fee = 5000 + (hours - 2) * 3000

print(fee)