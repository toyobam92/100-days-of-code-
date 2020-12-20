student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆
#TODO-1: Create an empty dictionary called student_grades.

student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇
for key in student_scores:
  grade_num = student_scores[key]
  if grade_num > 91 and grade_num < 100:
    student_grades[key] = "Outstanding"
  elif grade_num > 81 and grade_num < 90:
    student_grades[key] ="Exceeds Expectations"
  elif grade_num > 71 and grade_num < 80:
    student_grades[key] = "Acceptable"
  elif grade_num < 70:
    student_grades[key] = "Fail"
# 🚨 Don't change the code below 👇
print(student_grades)





