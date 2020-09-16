import math

n = int(input().strip())
grades = list()
finalGrades = list()
for i in range(n):
    grades.append(int(input().strip()))

for grade in grades:
    if grade < 38:
        finalGrades.append(grade)
    elif (math.ceil(grade / 5) * 5) - grade < 3:
        finalGrades.append(math.ceil(grade / 5) * 5)
    else:
        finalGrades.append(grade)

for g in finalGrades:
    print(g)

