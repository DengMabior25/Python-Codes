nums = [1, 1, 2, 2, 4, 4, 5, 6]
unique = []
for n in nums:
    if n not in unique:
        unique.append(n)
        print(unique)