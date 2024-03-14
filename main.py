import pandas

student_dict = {
    "student": ["Angela", "James", "Lilly"],
    "score": [56, 76, 98]
}

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

# Loop through a Data Frame
for (key, value) in student_data_frame.items():
    print(value)
