total_seconds = int(input("Enter the number of seconds: "))

hours = total_seconds // 3600
remaining_seconds = total_seconds % 3600
minutes = remaining_seconds // 60
seconds = remaining_seconds % 60

print(hours)
print(minutes)
print(seconds)