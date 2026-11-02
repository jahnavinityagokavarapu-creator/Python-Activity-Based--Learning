locations = []

n = int(input("Enter number of monitoring locations: "))

for i in range(n):
    name = input("\nEnter location name: ")

    count = int(input("Enter number of readings: "))
    readings = []

    for j in range(count):
        value = float(input(f"Enter reading {j + 1}: "))
        readings.append(value)

    locations.append([name, readings])

safe_limit = float(input("\nEnter safe threshold: "))
moderate_limit = float(input("Enter moderate threshold: "))

print("\n====== ENVIRONMENTAL MONITORING REPORT ======")


for location in locations:
    name = location[0]
    readings = location[1]

    if len(readings) == 0:
        print("\nLocation:", name)
        print("No readings available.")
        continue

    average = sum(readings) / len(readings)
    minimum = min(readings)
    maximum = max(readings)

  
    if average <= safe_limit:
        status = "SAFE"
    elif average <= moderate_limit:
        status = "MODERATE"
    else:
        status = "CRITICAL"

   
    print("\nLocation:", name)
    print("Readings:", readings)
    print("Average:", round(average, 2))
    print("Minimum:", minimum)
    print("Maximum:", maximum)
    print("Classification:", status)

print("\n============================================")
