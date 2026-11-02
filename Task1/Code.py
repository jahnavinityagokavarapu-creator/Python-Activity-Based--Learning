```python

students = ["Ravi", "Sita", "Kiran", "Priya"]

subjects = ["Python", "Maths", "Physics"]


marks = [
    [85, 78, 90],
    [65, 55, 60],
    [92, 88, 95],
    [70, 45, 50]
]

n = len(students)
m = len(subjects)

threshold = 60

print("STUDENT MARKS MATRIX ANALYSIS")
print("-" * 50)


print("\nMarks Matrix:")
print("Student", end="\t")

for subject in subjects:
    print(subject, end="\t")

print()

for i in range(n):
    print(students[i], end="\t")
    for j in range(m):
        print(marks[i][j], end="\t")
    print()

print("\n1. STUDENT-WISE STATISTICS")

averages = []

for i in range(n):
    total = sum(marks[i])
    average = total / m
    averages.append(average)

    print(students[i],
          "- Total:", total,
          "Average:", round(average, 2))


highest_average = max(averages)

print("\n2. TOP-PERFORMING STUDENT")

for i in range(n):
    if averages[i] == highest_average:
        print(students[i],
              "with average marks:",
              round(averages[i], 2))

print("\n3. SUBJECT-WISE STATISTICS")

subject_averages = []

for j in range(m):
    total = 0

    for i in range(n):
        total += marks[i][j]

    average = total / n
    subject_averages.append(average)

    print(subjects[j],
          "- Total:", total,
          "Average:", round(average, 2))


print("\n4. LOW-PERFORMING SUBJECTS")
print("(Average marks below", threshold, ")")

found = False

for j in range(m):
    if subject_averages[j] < threshold:
        print(subjects[j],
              "- Average:",
              round(subject_averages[j], 2))
        found = True

if not found:
    print("No low-performing subjects found.")
``` 
