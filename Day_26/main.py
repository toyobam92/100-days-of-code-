import random
import re

numbers = [1, 2, 3]
# new_list = []
# for n in list:
#     add_1 = n + 1
# new_list.append(add_1)
new_list = [n + 1 for n in numbers]
print(new_list)
# new_list = [new_item for item in list]
new_list = [numbers[::-1] for n in numbers]
print(new_list)

name = "Angela"
new_list = [letter for letter in name]
print(new_list)

num = range(1, 5)
double_num = [i * 2 for i in num]
print(double_num)

# conditional list comprehsion
# new_list = [new_item for item in list if test]

names = ["Pelumi", "Toyosi", "Funmi", "Dipo"]
short_names = [name.upper() for name in names if len(name) >= 5]
print(short_names)

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

squared_number = [num ** 2 for num in numbers]
print(squared_number)

even_number = [num for num in numbers if num % 2 == 0]
print(even_number)

with open("file_1.txt") as file_1:
    contents_1 = file_1.readlines()

with open("file_2.txt") as file_2:
    contents_2 = file_2.readlines()

common_num = [int(i.strip('\n')) for i in contents_1 if i in contents_2]
print(common_num)

# new_dict = {new_key:new_value for item in list}
# new_dict = {new_key:new_value for (key,value) in dict.items()}

names = ["Pelumi", "Toyosi", "Funmi", "Dipo"]

student_scores = {student: random.randint(60, 101) for student in names}

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
new_sentence = sentence.replace("?", "")
# Write your code below:
sentence_dict = {word: len(word) for word in new_sentence.split(' ')}
print(sentence_dict)

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
# 🚨 Don't change code above 👆
passed_students = {student: score for (student, score) in student_scores.items() if score >= 60}
print(passed_students)

weather_f = {day: (temp * 9 / 5 + 32) for (day, temp) in weather_c.items()}

# Write your code 👇 below:

print(weather_f)

import pandas as pd

student_data_frame = pd.DataFrame(student_dict)
#panda series object

for (index,row) in student_data_frame.iterrows():
    print(row.student)
    if row.student == "Angela"
        print(row.score)



