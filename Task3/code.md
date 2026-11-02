##Case Study: Employee Payroll and Deduction Analysis

##1. Problem Statement

Develop a Python program to calculate an employee's gross salary using basic pay, allowances, overtime payments, and incentives. Apply progressive deductions based on the gross salary and generate a formatted salary statement showing the employee's earnings, total deductions, and net salary.
 
 ##2. Algorithm
1. Start the program.
2. Input the employee's name and basic salary.
3. Input allowances, overtime hours, overtime rate per hour, and incentives.
4. Calculate the total allowances.
5. Calculate the overtime payment.
6. Calculate the gross salary.
7. Apply progressive deductions using the following example rates:
   - First ₹10,000: 0% deduction.
   - Next ₹10,000: 5% deduction.
   - Remaining amount above ₹20,000: 10% deduction.
8. Calculate the total deductions.
9. Calculate the net salary by subtracting deductions from gross salary.
10. Display the formatted salary statement.
11. Stop the program.
    
##3. Sample Input

Enter employee name: Ravi
Enter basic salary: 25000
Enter total allowances: 5000
Enter overtime hours: 10
Enter overtime rate per hour: 200
Enter incentives: 2000

##4. Sample Output

========== SALARY STATEMENT ==========
Employee Name       : Ravi
Basic Salary        : Rs. 25000.0
Allowances           : Rs. 5000.0
Overtime Pay         : Rs. 2000.0
Incentives           : Rs. 2000.0
--------------------------------------
Gross Salary         : Rs. 34000.0
Total Deductions     : Rs. 1900.0
Net Salary           : Rs. 32100.0
======================================

Calculation
Step 1: Calculate overtime pay

Overtime Pay = 10 × ₹200 = ₹2,000

Step 2: Calculate gross salary

Gross Salary = ₹25,000 + ₹5,000 + ₹2,000 + ₹2,000

Gross Salary = ₹34,000

Step 3: Calculate progressive deductions
- First ₹10,000: ₹0 deduction
- Next ₹10,000: ₹10,000 × 5% = ₹500
- Remaining ₹14,000: ₹14,000 × 10% = ₹1,400
Total Deductions = ₹500 + ₹1,400 = ₹1,900

Step 4: Calculate net salary

Net Salary = ₹34,000 − ₹1,900 = ₹32,100


##5. Mermaid Flowchart Code
Copy this code into a Mermaid-compatible editor to generate the flowchart.

flowchart TD

    A([Start]) --> B[/Input employee details/]
    B --> C[Calculate overtime pay]
    C --> D[Calculate gross salary]
    D --> E{Gross salary <= 10000?}

    E -- Yes --> F[Deduction = 0]
    E -- No --> G{Gross salary <= 20000?}

    G -- Yes --> H[Deduction = 5% of amount above 10000]
    G -- No --> I[Deduction = 500 + 10% of amount above 20000]

    F --> J[Calculate net salary]
    H --> J
    I --> J

    J --> K[/Display formatted salary statement/]
    K --> L([Stop])
    
##6. Conclusion

The Employee Payroll and Deduction Analysis program calculates gross salary from basic pay, allowances, overtime payments, and incentives. It applies progressive deductions and calculates the final net salary. The program demonstrates Python variables, arithmetic operators, conditional statements, and formatted output.
