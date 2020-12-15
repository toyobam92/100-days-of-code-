import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(",")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

start = 0
stop = len(names) - 1

name_checker = random.randint(start, stop)

payer = names[name_checker]

print(f"{payer} is going to to buy the meal today!")

#person_paying = random.choice(names)
