##5. Multi-Plan Telecommunications Cost Optimization

##1. Problem Statement

Evaluate several mobile plans against data usage, validity, and budget constraints. Calculate excess data charges
and identify the most economical eligible plan.
Assumptions / Rules
Example plans: Plan A n199 for 2 GB and 28 days; Plan B n299 for 3 GB and 28 days; Plan C n399 for 5 GB and 56
days. Excess data costs n50 per GB. The total plan cost must fit the budget.

##2. Algorithm

1. Start.
2. Read expected data usage, required validity, and budget.
3. Store the available plans with price, data limit, and validity.
4. For each plan, check whether validity is sufficient.
5. Calculate excess data cost and total cost.
6. Keep the cheapest plan whose total cost is within budget.
7. Display the selected plan or report that no plan is eligible.
8. Stop

   ##3. Mermaid Flowchart Code
   
flowchart TD

    N0(["START"])
    N1["Input data usage, required validity, and budget"]
    N0 --> N1
    N2["Load the three mobile plans"]
    N1 --> N2
    N3["Check each plan's validity"]
    N2 --> N3
    N4["Calculate excess data charge and total cost"]
    N3 --> N4
    N5{"Is total cost within budget?"}
    N4 --> N5
    N6["Yes fi Compare with cheapest eligible plan; No fi Skip plan"]
    N5 -->|Yes / No as applicable| N6
    N7["After all plans, display cheapest eligible plan or no match"]
    N6 --> N7
    N8(["STOP"])
    N7 --> N8
    
##4. Pseudocode

START
INPUT usage_GB, required_days, budget
plans = [(A,199,2,28), (B,299,3,28), (C,399,5,56)]
best_plan = NONE
best_cost = infinity
FOR each plan
    IF plan.validity >= required_days
        extra_GB = MAX(0, usage_GB - plan.data_limit)
        total_cost = plan.price + extra_GB * 50
        IF total_cost <= budget AND total_cost < best_cost
            best_plan = plan.name
            best_cost = total_cost
        END IF
    END IF
END FOR
IF best_plan exists
    DISPLAY best_plan, best_cost
ELSE
    DISPLAY "No eligible plan"
END IF
STOP

##5. Sample Input

Enter data usage in GB: 2.5
Enter required validity: 28
Enter budget: 400

##6. Sample Output

Best Plan: Plan A
Total Cost: Rs. 224.0

##7. Conclusion

The program compares mobile plans using usage, validity, and budget. It calculates excess data charges and selects
the lowest-cost eligible plan
