usage = float(input("Enter electricity usage in kwh: "))
if usage <= 100:
    total_bills = usage * 0.10
elif usage <= 300:
    total_bills = 10 + (usage - 100) * 0.15
else:
    total_bills = 10 + 30 (usage - 300) * 0.20

print(total_bills)

    