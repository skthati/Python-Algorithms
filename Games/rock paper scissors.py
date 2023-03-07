import random

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

#Write your code below this line 👇


player_choice = input("rock, paper, scissors, Enter your choice: ")

print(f"Your choice is: {player_choice}")
if player_choice == "rock":
  print(rock)
elif player_choice == "paper":
  print(paper)
else:
  print(scissors)

all_list = ['rock', 'paper', 'scissors']
computer_choice = random.choice(all_list)

print(f"Computer choice is: {computer_choice}")

if computer_choice == "rock":
  print(rock)
elif computer_choice == "paper":
  print(paper)
else:
  print(scissors)

if player_choice == computer_choice:
  print("Draw")
elif player_choice == "rock" and (computer_choice == "scissors"):
  print("Player wins!")
elif player_choice == "paper" and (computer_choice == 'rock'):
  print('Player wins')
elif player_choice == "scissors" and (computer_choice == 'paper'):
  print("Player wins!")
else:
  print("Computer wins!")
  