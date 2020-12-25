import game_data
import random
from replit import clear

import art 

print(art.logo)
score = 0
game_on = True

data = game_data.data

account_b = random.choice(data)

while game_on:
  account_a = account_b
  account_b = random.choice(data)

  while account_a == account_b:
    account_b = random.choice(data)

  def dataset(account):
    names = account['name']
    descriptions =account['description']
    countrys = account['country']
    return(f" {names},{descriptions}, from {countrys}.")

  print(f"Compare A:{dataset(account = account_a)}")
  print(art.vs)
  print(f"Against B:{dataset(account = account_b)}")

  guess = input("Who has more followers?,Type 'A' or 'B':").lower()

  a_follower_count = account_a['follower_count']
  b_follower_count = account_b['follower_count']


  def check(guess,a_follower_count,b_follower_count):
        if a_follower_count > b_follower_count:
            return guess == "a"
        else:
            return guess == "b"

  is_correct = check(guess,a_follower_count,b_follower_count)
  
  clear()

  if is_correct:
    score +=1
    print(f"Youre right! Current score:{score}")
  else:
    game_on = False
    print(f"Sorry You're wrong, Your final score is {score}")
    play_again = input("Will you like to play again?, Try 'y' or 'n'")
      if play_again == 'y':
        game_on = True



# game_on = True

# while game_on:
#   data = game_data.data
#   score = 0
#   x = random.choice(data)
#   names = x['name']
#   descriptions = x['description']
#   countrys = x['country']
#   follower_count = x['follower_count']
#       #follower_count =  random_shuffle(data)['follower_count']

#   y = random.choice(data)
#   comp_names = y['name']
#   comp_descriptions = y['description']
#   comp_countrys =  y['country']
#   comp_follower_count = y['follower_count']

#   print(f"Compare A: {names},{descriptions}, from {countrys}.")
#   print(f"Compare B: {comp_names},{comp_descriptions}, from {comp_countrys}.")

#   higher_lower = input("Who has more followers?,Type 'A' or 'B':")
  
#   if higher_lower == "A"and follower_count > comp_follower_count:
#         score +=1
#         print(f"You're right! Current Score:{score}")
#   elif higher_lower == "B" and comp_follower_count > follower_count:
#         score +=1
#         print(f"You're right! Current Score:{score}")
#   else:
#           game_on = False
#           print(f"Sorry thats wrong.Final score {score}")
 
