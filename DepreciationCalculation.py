initial_price = 12000000
salvage_value = 2000000
economic_life = 4

annual_depreciation = (initial_price - salvage_value) / economic_life

years_passed = 2
value_after_2_years = initial_price - (annual_depreciation * years_passed)

print(annual_depreciation)
print(years_passed)