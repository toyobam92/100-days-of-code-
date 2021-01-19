# student_dict = {
#     "student": ["Angela", "James", "Lily"],
#     "score": [56, 76, 98]
# }
#
# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass
#
# import pandas
# student_data_frame = pandas.DataFrame(student_dict)
#
# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass
#
# # Keyword Method with iterrows()
# # {new_key:new_value for (index, row) in df.iterrows()}

# #TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

import pandas as pd
npa = pd.read_csv('nato_phonetic_alphabet.csv')
nato_alphabet= {row.letter : row.code for (index, row) in npa.iterrows()}


user_prompt = input("Enter a word:").upper()
word = [each_word for each_word in user_prompt]

word_list = [nato_alphabet[i] for i in word if i in nato_alphabet.keys()]
print(word_list)

# #TODO 2. Create a list of the phonetic code words from a word that the user inputs.
#
