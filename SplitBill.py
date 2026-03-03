bill = float(input("Enter the total bills: "))
people = float(input("Enter the number of people:"))

tax_rate = 0.10
total_after_tax = bill * (1 + tax_rate)
pay_per_person = total_after_tax / people

print(total_after_tax)
print(pay_per_person)