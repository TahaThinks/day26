import random
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
students_score = {student:random.randint(1, 100) for student in names}
print(students_score)