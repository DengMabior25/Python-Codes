distance = float(input("Enter distance traveled (km): "))
time = float(input("Enter travel time (hours): "))

speed = distance / time

print(f"Average speed: {speed:.2(km/h)}")

if speed > 80:
    print("High speed")