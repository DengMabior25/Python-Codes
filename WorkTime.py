rate = float(input("Enter hourly rate: "))
hours = float(input("Enter total hours: "))
minutes = float(input("Enter total minutes: "))

total_hours = hours + (minutes / 60)
total_payment = total_hours * rate

print(total_payment)