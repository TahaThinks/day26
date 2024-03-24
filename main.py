import pandas

# Create a DataFrame from a csv file:
nato_phonetic_data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(nato_phonetic_data_frame)

# Create a dictionary from DataFrame:
nato_phonetic_dict = {row.letter: row.code for (index, row) in nato_phonetic_data_frame.iterrows()}
# print(nato_phonetic_dict)

def generate_photenic():
    word = input("Enter a Word: ").upper()
    # print(word)
    try:
        word_phonetic = [nato_phonetic_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please")
        generate_photenic()
    else:
        print(word_phonetic)

generate_photenic()