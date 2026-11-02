name = input("Enter employee name: ")
basic = float(input("Enter basic salary: "))
allowances = float(input("Enter total allowances: "))
overtime_hours = float(input("Enter overtime hours: "))
overtime_rate = float(input("Enter overtime rate per hour: "))
incentives = float(input("Enter incentives: "))

overtime_pay = overtime_hours * overtime_rate
gross_salary = basic + allowances + overtime_pay + incentives

if gross_salary <= 10000:
    deduction = 0
elif gross_salary <= 20000:
    deduction = (gross_salary - 10000) * 0.05
else:
    deduction = (10000 * 0.05) + \
                ((gross_salary - 20000) * 0.10)


net_salary = gross_salary - deduction

print("\n========== SALARY STATEMENT ==========")
print("Employee Name       :", name)
print("Basic Salary        : Rs.", round(basic, 2))
print("Allowances           : Rs.", round(allowances, 2))
print("Overtime Pay         : Rs.", round(overtime_pay, 2))
print("Incentives           : Rs.", round(incentives, 2))
print("--------------------------------------")
print("Gross Salary         : Rs.", round(gross_salary, 2))
print("Total Deductions     : Rs.", round(deduction, 2))
print("Net Salary           : Rs.", round(net_salary, 2))
print("======================================")
