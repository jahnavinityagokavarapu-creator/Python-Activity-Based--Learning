##4. Employee Payroll and Deduction Analysis

##1. Problem Statement

Calculate gross salary from basic pay, allowances, overtime, and incentives. Apply progressive deductions and
generate a formatted salary statement.
Assumptions / Rules
Example policy: HRA 20% of basic pay, DA 10% of basic pay, overtime n100/hour, incentive n1,000, PF 12% of
basic pay, and tax 5% of gross salary.

##2. Algorithm

1. Start.
2. Read employee name, basic salary, and overtime hours.
3. Calculate HRA, DA, overtime payment, and incentive.
4. Add these amounts to basic salary to obtain gross salary.
5. Calculate PF and tax deductions.
6. Subtract total deductions from gross salary.
7. Display the salary statement.
8. Stop.
9. 
   ##3. Mermaid Flowchart Code
flowchart TD
    N0(["START"])
    N1["Input employee name, basic salary, and overtime hours"]
    N0 --> N1
    N2["Calculate HRA, DA, overtime, and incentive"]
    N1 --> N2
    N3["Calculate gross salary"]
    N2 --> N3
    N4["Calculate PF and tax deductions"]
    N3 --> N4
    N5["Calculate net salary"]
    N4 --> N5
    N6["Display salary statement"]
    N5 --> N6
    N7(["STOP"])
    N6 --> N7

##4. Pseudocode

START
INPUT name, basic_salary, overtime_hours
HRA = basic_salary * 0.20
DA = basic_salary * 0.10
overtime = overtime_hours * 100
incentive = 1000
gross = basic_salary + HRA + DA + overtime + incentive
PF = basic_salary * 0.12
tax = gross * 0.05
deduction = PF + tax
net_salary = gross - deduction
DISPLAY gross, deduction, net_salary
STOP

##5. Sample Input

Enter employee name: Priya
Enter basic salary: 20000
Enter overtime hours: 5

##6. Sample Output

Employee Salary Statement
Name: Priya
Basic Salary: 20000.0
HRA: 4000.0
DA: 2000.0
Overtime: 500.0
Incentive: 1000
Gross Salary: 27500.0
Total Deduction: 3775.0
Net Salary: 23725.0

##7. Conclusion

The program calculates employee gross salary, allowances, overtime, incentives, and deductions, then produces the
final net salary statement
