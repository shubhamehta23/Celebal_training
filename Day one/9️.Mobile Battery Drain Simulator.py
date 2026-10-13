
battery_percentage = 100
battery_drain_per_minute = int(input("Enter battery drain per minute: "))

minutes = 0

while battery_percentage > 0:
    battery_percentage = battery_percentage - battery_drain_per_minute
    minutes = minutes + 1

print("Battery lasts for", minutes, "minutes")
