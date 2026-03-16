salary = float(input("Enter employee salary: "))
years_of_services = float(input("Enter years of services: "))
if years_of_services >= 10:
    bonus = salary * 0.25
elif years_of_services >= 5:
    bonus = salary * 0.15
elif years_of_services >= 1:
    bonus = salary * 0.05
else:
    bonus = 0

print(bonus)