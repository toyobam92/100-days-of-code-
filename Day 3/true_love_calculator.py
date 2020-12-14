# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

first_name = name1.lower()
second_name = name2.lower()
love_name = first_name + second_name

t =love_name.count("t")
r =love_name.count("r")
u =love_name.count("u")
e = love_name.count("e")

true = t + r + u + e
strue = str(true)
l = love_name.count("l")
o = love_name.count("o")
v =love_name.count("v")
e = love_name.count("e")

love = l + o + v + e
slove = str(love)

score = strue + slove
print(score)
int_score = int(score)
print(int_score)

if int_score < 10 or int_score > 90:
  print(f"Your score is {int_score}%, you go together like coke and mentos.") 
elif int_score >= 40 and int_score <= 50:
  print(f"Your score is {int_score}%, you are alright together.")
else:
  print(f"Your score is {int_score}%")




