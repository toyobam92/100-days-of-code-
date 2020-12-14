# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

small_pizza = 15
medium_pizza = 20
large_pizza = 25

p_small = 2
p_m_l = 3

add_cheese = 1 
bill = 0

if size == "L":
  bill = large_pizza
elif size =="M":
  bill = medium_pizza
elif size == "S":
  bill = small_pizza

if add_pepperoni == "Y":
  if size == "S":
    bill = bill + p_small
  else:
    bill = bill + p_m_l

if extra_cheese == "Y":
  bill += add_cheese

print(f"Your total pizza bill is ${bill}") 

#LOGICAL OPERTORS
 #AND, OR , NOT 







