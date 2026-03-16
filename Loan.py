salary = float(input("Enter your salary: "))
credit_score = int(input("Enter your credit score: "))
employment_duration = int(input("Enter employment duration in years: "))

cond1 = salary >= 3000
cond2 = credit_score >= 650
cond3 = employment_duration >= 2

satisfied_count =sum([cond1, cond2, cond3])
if satisfied_count == 3:
    print("Decision: Loan Approved")
elif satisfied_count == 2:
    print("Decision: Conditional Approved")
else:
    print("Decision:Loan Rejected")