 name = input("Enter route name: ")
    demand = int(input("Enter passenger demand: "))
    buses = int(input("Enter available buses: "))

    if demand < 0 or buses < 0:
        print("Invalid demand or bus count!")
        break

    routes.append(name)
    demands.append(demand)
    available_buses.append(buses)

else:
    total_required = 0
    total_available = 0
    total_unserved = 0

    print("\n===== CAMPUS TRANSPORT REPORT =====")

    for i in range(n):
        demand = demands[i]
        available = available_buses[i]

       
        required = (demand + capacity - 1) // capacity

      
        served = min(demand, available * capacity)

        unserved = demand - served

        total_required += required
        total_available += available
        total_unserved += unserved

        print("\nRoute:", routes[i])
        print("Passenger Demand:", demand)
        print("Buses Required:", required)
        print("Available Buses:", available)
        print("Passengers Accommodated:", served)
        print("Unserved Passengers:", unserved)

    print("\n===== TOTAL SUMMARY =====")
    print("Total Buses Required:", total_required)
    print("Total Buses Available:", total_available)
    print("Total Unserved Passengers:", total_unser
