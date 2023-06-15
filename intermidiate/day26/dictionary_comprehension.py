# Dictionary Comprehension
import random

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
student_scores = {name: random.randint(1, 100) for name in names}

passed_students = {student: scores for (student, scores) in student_scores.items() if scores > 64}
print(passed_students)