# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
total = 0
num_students =0
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
  total = total + student_heights[n] 
  num_students = n + 1
  average_height = round(total/y)
print(f"The average height is {average_height}")
#Write your code below this row 👇
