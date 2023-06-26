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

game_images = [rock, paper, scissors]

player = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n'))
computer = random.randint(0,2)

if player >= 3 or player < 0:
  print('You typed an invalid number. You lose.')
else:
  print(game_images[player])

  print("Computer chose:")

  print(game_images[computer])

  if player == 0 and computer == 2:
   print('You win!')
  elif player == 2 and computer == 0:
   print('You lose')
  elif player < computer:
   print('You lose.')
  elif player == computer:
   print("It's a draw.")
  elif player > computer:
   print('You win!')