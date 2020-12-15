mport random

user_choice = int(input("What do you want to choose?\nType 0 for Rock, 1 for Paper and 2 for Scissors\n"))

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#game_images = [rock,paper,scissors]
#if user_choice >= 3 or user_choice < 0:
   #print("You typed an invalid number, You lose!")
#else:
  #print(game_images[user_choice])
  #tab subsequent code

#User input
if user_choice == 0:
  print(rock)
elif user_choice == 1:
  print(paper)
elif user_choice == 2:
  print(scissors)

#print(game_images[computer_choice])

#Computer input
start = 0
stop = 2

computer_choice = random.randint(start, stop)

print(f"Computer chose {computer_choice}")

if computer_choice == 0:
  print(rock)
elif computer_choice == 1:
  print(paper)
elif computer_choice == 2:
  print(scissors)


if user_choice >= 3 or user_choice < 0:
   print("You typed an invalid number, You lose!")
elif user_choice == 0 and computer_choice == 2:
  print("You win")
elif user_choice == 2 and computer_choice == 1:
  print("You win")
elif user_choice == 1 and computer_choice == 0:
  print("You win")
elif user_choice == 0 and computer_choice == 0:
  print("It's a draw")
elif user_choice == 1 and computer_choice == 1:
  print("It's a draw")
elif user_choice == 2 and computer_choice  == 2:
  print("Its a draw")
else:
  print("You lose!")
