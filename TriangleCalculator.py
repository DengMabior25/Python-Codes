s1 = float(input("Enter length of side 1: "))
s2 = float(input("Enter length of side 2: "))
s3 = float(input("Enter length of side 3: "))
if s1 == s2 == s3:
    triangle_type = "Equilateral"
elif s1 == s2 or s1 == s3 or s2 == s3:
    triangle_type = "Isosceles"
else:
    triangle_type = "Scalene"

print(triangle_type)