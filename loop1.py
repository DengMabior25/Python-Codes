rows = 4
cols = 5
mid = cols // 2

for i in range(rows):
    for j in range(cols):
        if j == mid or (i in [1, 2] and j in [1, 2, 3]):
            print("0", end=" ")
        else:
            print("X", end=" ")
    print()