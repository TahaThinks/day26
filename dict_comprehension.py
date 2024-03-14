# import random
# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# students_score = {student:random.randint(1, 100) for student in names}
# print(students_score)
#
# passed_students = {student:score for (student,score) in students_score.items() if score>60}
# print(passed_students)
#
# sentence = "What is the Airspeed velocity of an Unladen Swallow?"
#
# words_list = [word for word in sentence.split()]
# print(words_list)
# words_dict = {word:len(word) for word in words_list}
# print(words_dict)

# student_dict = {
#     "student": ["Angela", "James", "Lilly"],
#     "score": [56, 76, 98]
# }
# # Looping through dictionaries
# for (key, value) in student_dict.items():
#     print(key)


# student_dict = {
#     "student": ["Angela", "James", "Lilly"],
#     "score": [56, 76, 98]
# }
#
# student_data_frame = pandas.DataFrame(student_dict)
# print(student_data_frame)
#
# # # Loop through a Data Frame
# # for (key, value) in student_data_frame.items():
# #     print(value)
#
# # Loop through rows of a data frame
#
# for (index, row) in student_data_frame.iterrows():
#     if row.student == "Angela":
#         print(row.score)