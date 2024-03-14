import pandas

# Create a DataFrame from a csv file:
nato_phonetic_data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(nato_phonetic_data_frame)

# Create a dictionary from DataFrame:
nato_phonetic_dict = {row.letter: row.code for (index, row) in nato_phonetic_data_frame.iterrows()}
# print(nato_phonetic_dict)

word = input("Enter a Word: ").upper()
# print(word)