##3. Hospital Billing and Patient Classification

##1. Problem Statement

Process consultation, diagnostic, and treatment charges, apply concessions, validate billing constraints, and classify
patients according to a supplied payment policy.
Assumptions / Rules
Example charges: consultation n500, diagnostics n1,000, treatment n3,000. A valid insurance card gives 20%
discount. Otherwise, patients aged 60 or above receive 10%. Only the highest applicable discount is applied.

##2. Algorithm

1. Start.
2. Read patient name, age, and insurance status.
3. Set consultation, diagnostic, and treatment charges.
4. Calculate the total bill.
5. If insurance is valid, apply 20% discount; otherwise, if age is at least 60, apply 10%; otherwise, no discount.
6. Calculate final bill and classify the patient.
7. Display the bill.
8. Stop

   ##3. Mermaid Flowchart Code
   
flowchart TD
    N0(["START"])
    N1["Input patient name, age, and insurance status"]
    N0 --> N1
    N2["Add consultation, diagnostic, and treatment charges"]
    N1 --> N2
    N3{"Is insurance valid?"}
    N2 --> N3
    N4["Yes fi Apply 20% discount; No fi Check age"]
    N3 -->|Yes / No as applicable| N4
    N5{"Is age 60 or above?"}
    N4 --> N5
    N6["Yes fi Apply 10%; No fi No discount"]
Page 7
Python Activity-Based Learning | Case Studies 1–10
    N5 -->|Yes / No as applicable| N6
    N7["Calculate final bill and display patient category"]
    N6 --> N7
    N8(["STOP"])
    N7 --> N8
##4. Pseudocode

START
INPUT name, age, insurance_status
consultation = 500
diagnostic = 1000
treatment = 3000
total = consultation + diagnostic + treatment
IF insurance_status is "yes"
    discount = total * 0.20
    category = "Insured Patient"
ELSE IF age >= 60
    discount = total * 0.10
    category = "Senior Citizen"
ELSE
    discount = 0
    category = "Normal Patient"
END IF
final_bill = total - discount
DISPLAY name, category, total, discount, final_bill
STOP

##5. Sample Input

Enter patient name: Ravi
Enter patient age: 65
Valid insurance? (yes/no): no

##6. Sample Output
Hospital Bill
Patient: Ravi
Category: Senior Citizen
Total: 4500
Discount: 450.0
Final Bill: 4050.0

##7. Conclusion
The program calculates hospital charges, applies the correct concession based on insurance or age, and displays the
patient's final payable amount
