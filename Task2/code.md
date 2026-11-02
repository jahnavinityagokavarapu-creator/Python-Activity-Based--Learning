##2. Progressive Electricity Billing

##1. Problem Statement

Calculate household electricity bills using multiple consumption slabs, fixed charges, surcharges, and rebates.
Compare bills across months and identify unusual increases.
Assumptions / Rules
Example tariff: first 100 units at n2/unit; next 100 units at n3/unit; units above 200 at n5/unit. Fixed charge n50;
surcharge 5% of energy charge; rebate n20 when consumption is below 100 units. An increase greater than 50%
over the previous bill is unusual.

##2. Algorithm

1. Start.
2. Read the number of months.
3. For each month, read units consumed.
4. Calculate energy charges using the applicable slabs.
5. Add fixed charge and 5% surcharge; subtract n20 rebate if units are below 100.
6. Store and display the bill.
7. From the second month onward, compare the bill with the previous month's bill.
8. If the increase is greater than 50%, report an unusual increase.
9. Stop
10. 
3.## Mermaid Flowchart Code

flowchart TD

    N0(["START"])
    N1["Input number of months and monthly units"]
    N0 --> N1
    N2["Calculate slab-wise energy charge"]
    N1 --> N2
    N3["Add fixed charge and surcharge; apply rebate if eligible"]
    N2 --> N3
    N4["Calculate and store the monthly bill"]
    N3 --> N4
    N5{"Is this not the first month?"}
    N4 --> N5
    N6["If yes, compare with previous bill and flag increase > 50%"]
    N5 -->|Yes / No as applicable| N6
    N7["Display bill; repeat for remaining months"]
    N6 --> N7
    N8(["STOP"])
    N7 --> N8
    
   ##4.sample input
   
Enter number of months: 3
Enter units consumed: 80
Enter units consumed: 150
Enter units consumed: 250

##5. Sample Output

Month 1 Bill: Rs. 238.0
Month 2 Bill: Rs. 523.0
Unusual increase detected
Month 3 Bill: Rs. 1039.5
Unusual increase detected

##6. Conclusion

The program calculates monthly electricity bills using progressive slabs and additional charges. It also compares bills
and detects unusually large increases
