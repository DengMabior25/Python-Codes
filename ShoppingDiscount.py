purchase_amount = float(input("Enter the total purchase amount: "))

if purchase_amount >= 500000:
    discount_rate = 0.10
elif purchase_amount >= 250000:
    discount_rate = 0.05
else:
    discount_rate = 0.0

discount_amount = purchase_amount * discount_rate
final_amount = purchase_amount - discount_amount

print(discount_amount)
print(final_amount)

