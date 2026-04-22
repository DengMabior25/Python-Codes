size = 5
mid = size // 2
for i in range(size):
    for j in range(size):
        if j == mid:
            print("0", end=" ")
        else:
            print("X", end=" ")
    print()
