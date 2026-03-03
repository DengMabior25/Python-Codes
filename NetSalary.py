base_salary = 5000000
allowance = 750000

bpjs = 0.02 * base_salary
tax = 0.05 * base_salary
total_deductions = bpjs + tax

net_salary = base_salary + allowance - total_deductions

print(net_salary)