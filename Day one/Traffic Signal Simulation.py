
time_in_seconds = int(input("Enter time in seconds: "))

time_in_seconds = (time_in_seconds - 1) % 90 + 1

if time_in_seconds <= 30:
    print("RED")
elif time_in_seconds <= 45:
    print("YELLOW")
else:
    print("GREEN")
