student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = {}

for key in student_scores:
    if 90 < student_scores[key] <= 100:
        student_grades[key] = "Outstanding"
    elif 80 < student_scores[key] <= 90:
        student_grades[key] = "Exceeds expectations"
    elif 70 < student_scores[key] <= 80:
        student_grades[key] = "Acceptable"
    elif student_scores[key] <= 70:
        student_grades[key] = "Fail"

print(student_scores)

print(student_grades)