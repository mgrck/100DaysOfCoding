from random import randint
from art import logo
number = randint(1,101)
print(logo)
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard': ")

if difficulty_level == 'easy':
  attempts_remaining = 10
elif difficulty_level == 'hard':
  attempts_remaining = 5

while attempts_remaining > 0:
  print(f"You have {attempts_remaining} attempts remaining to guess the number.")
  player_guess = int(input("Make a guess: "))
  if player_guess == number:
    print(f"You got it! The answer was {number}.")
    break
  else:
    if player_guess > number:
      attempts_remaining -= 1
      if attempts_remaining == 0:
        break
      else:
        print("Too high.\nGuess again.")
    elif player_guess < number:
      attempts_remaining -= 1
      if attempts_remaining == 0:
        break
      else:
        print("Too low.\nGuess again.")
      
if attempts_remaining == 0:
  print("You've run out of guesses. You lose.")