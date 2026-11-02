##9.Environmental Monitoring Data Analyzer

##1. Problem Statement

The Environmental Monitoring Data Analyzer is a Python program designed to analyze air-quality or water-quality readings stored in nested lists. It calculates the average, minimum, and maximum values for each monitoring location and classifies the observations using user-supplied threshold values.

The program helps identify whether environmental conditions are Safe, Moderate, or Critical based on the average reading.

##2. Algorithm

1. Start the program.
2. Enter the number of monitoring locations.
3. For each location, enter its name and environmental readings.
4. Store the readings in a nested list.
5. Enter the safe and moderate threshold values.
6. Calculate the average, minimum, and maximum readings for each location.
7. Classify each location:
   - Safe: Average is less than or equal to the safe threshold.
   - Moderate: Average is greater than the safe threshold but less than or equal to the moderate threshold.
   - Critical: Average is greater than the moderate threshold.
8. Display the readings, average, minimum, maximum, and classification for each location.
9. Stop the program.
    
    ##3. Sample Input
   
Enter number of monitoring locations: 3

Enter location name: Vijayawada
Enter number of readings: 4
Enter reading 1: 35
Enter reading 2: 40
Enter reading 3: 45
Enter reading 4: 40

Enter location name: Guntur
Enter number of readings: 4
Enter reading 1: 60
Enter reading 2: 65
Enter reading 3: 70
Enter reading 4: 65

Enter location name: Visakhapatnam
Enter number of readings: 4
Enter reading 1: 90
Enter reading 2: 95
Enter reading 3: 100
Enter reading 4: 95

Enter safe threshold: 50
Enter moderate threshold: 80

##4. Sample Output

====== ENVIRONMENTAL MONITORING REPORT ======

Location: Vijayawada
Readings: [35.0, 40.0, 45.0, 40.0]
Average: 40.0
Minimum: 35.0
Maximum: 45.0
Classification: SAFE

Location: Guntur
Readings: [60.0, 65.0, 70.0, 65.0]
Average: 65.0
Minimum: 60.0
Maximum: 70.0
Classification: MODERATE

Location: Visakhapatnam
Readings: [90.0, 95.0, 100.0, 95.0]
Average: 95.0
Minimum: 90.0
Maximum: 100.0
Classification: CRITICAL

============================================

Explanation of Results
- Vijayawada: Average = (35 + 40 + 45 + 40) / 4 = 40.0, so the classification is Safe.
- Guntur: Average = (60 + 65 + 70 + 65) / 4 = 65.0, so the classification is Moderate.
- Visakhapatnam: Average = (90 + 95 + 100 + 95) / 4 = 95.0, so the classification is Critical.
- 
##5. Mermaid Flowchart Code

Copy this code into the Mermaid Live Editor to generate a visual flowchart.

flowchart TD

    A([Start]) --> B[/Enter number of locations/]
    B --> C[/Enter location names and readings/]
    C --> D[/Enter safe and moderate thresholds/]
    D --> E[Calculate average, minimum and maximum]
    E --> F{Average <= safe threshold?}
    F -- Yes --> G[Classification = SAFE]
    F -- No --> H{Average <= moderate threshold?}
    H -- Yes --> I[Classification = MODERATE]
    H -- No --> J[Classification = CRITICAL]
    G --> K[Display monitoring report]
    I --> K
    J --> K
    K --> L{More locations to process?}
    L -- Yes --> E
    L -- No --> M([Stop])


##5.Conclusion: 
This program uses nested lists and basic Python functions to analyze environmental readings, calculate statistical values, and classify monitoring locations according to user-defined thresholds.
