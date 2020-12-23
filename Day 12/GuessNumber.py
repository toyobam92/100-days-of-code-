import random

targetNum = random.randint(1, 101)
print("Welcome to the Number Guessing Game")
print("I'm thinking of a number between 1 and 100")
print(f"Psst, the correct answer is {targetNum}")

game_difficulty = input("Type 'easy' or 'hard': ")
game_on = True

def guess_game(attempts,targetNum):
  game_on = True
  print(f"You have {attempts} attempts remaining to guess the number ")
  number = int(input("Make a guess:")) 
  while game_on:
    if number!=targetNum:
      attempts -= 1
      print(f"You have {attempts} attempts remaining to guess the number")
    if number < targetNum:
        print("Too low \nGuess again")
        number = int(input("Make a guess:"))
    elif number >  targetNum:
        print("Too high\nGuess again")
        number  = int(input("Make a guess:"))
    elif number == targetNum:
        game_on = False
        print("You guessed the right number, game over")
    if attempts == 1:
        game_on  = False
        print("You've run out of guess you lose")

if game_difficulty == 'easy':
   attempts = 10 
   guess_game(attempts,targetNum)
else:
   attempts = 5
   guess_game(attempts,targetNum)
