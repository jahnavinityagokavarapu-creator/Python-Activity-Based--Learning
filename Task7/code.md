##6. Railway Fare and Reservation Calculator

##1. Problem Statement

Calculate fares for multiple passengers using distance, travel classes, age-based concessions, reservation fees, and
cancellation penalties.
Assumptions / Rules
Example policy: base fare n2/km; AC multiplier 2 and sleeper multiplier 1; under age 5 travels free; age 5–12 gets
50% concession; age 60 or above gets 20% concession; reservation fee n30 when fare is payable; cancellation
penalty is 10% of the calculated ticket amount.

##2. Algorithm

1. Start.
2. Read number of passengers.
3. For each passenger, read name, age, distance, travel class, and cancellation choice.
4. Calculate base fare and apply class multiplier.
5. Apply age-based concession.
6. Add reservation fee if fare is payable.
7. If cancelled, calculate 10% cancellation penalty; otherwise show ticket fare.
8. Repeat for all passengers and stop
   
   ##3. Mermaid Flowchart Code
   
flowchart TD
    N0(["START"])
    N1["Input passenger count and passenger details"]
    N0 --> N1
    N2["Calculate distance fare and class multiplier"]
    N1 --> N2
    N3{"What is the passenger age category?"}
    N2 --> N3
    N4["Apply free fare, 50% concession, 20% concession, or full fare"]
    N3 -->|Yes / No as applicable| N4
    N5["Add reservation fee when applicable"]
    N4 --> N5
    N6{"Is ticket cancelled?"}
    N5 --> N6
    N7["Yes fi Calculate 10% penalty; No fi Keep ticket fare"]
    N6 -->|Yes / No as applicable| N7
    N8["Display passenger fare; repeat for next passenger"]
    N7 --> N8
    N9(["STOP"])
    N8 --> N9
    
##4. Pseudocode

START
INPUT number_of_passengers
FOR each passenger
    INPUT name, age, distance, travel_class, cancel
    fare = distance * 2
    IF travel_class == "ac"
        fare = fare * 2
    END IF
    IF age < 5
        fare = 0
    ELSE IF age <= 12
        fare = fare * 0.50
    ELSE IF age >= 60
        fare = fare * 0.80
    END IF
    IF fare > 0
        fare = fare + 30
    END IF
    IF cancel == "yes"
        fare = fare * 0.10
        DISPLAY cancellation penalty
    ELSE
        DISPLAY ticket fare
    END IF
END FOR
STOP

##5. Sample Input

Enter number of passengers: 1
Passenger 1
Enter name: Ravi
Enter age: 65
Enter distance: 100
Enter class (sleeper/ac): sleeper
Cancel ticket? (yes/no): no

##6. Sample Output

Passenger: Ravi
Ticket fare: 190.0

##7. Conclusion

The program calculates railway fares by considering distance, travel class, age concessions, reservation charges,
and cancellation penalties
