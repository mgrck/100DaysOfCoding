############### Blackjack Project #########################

############### Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

###########################################################

import random
from replit import clear
from art import logo
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

def change_11_into_1(set_cards):
  for i in range(0,len(set_cards)):
    if set_cards[i] == 11:
      set_cards[i] = 1

def calculate_score(set_cards):
  return sum(set_cards)

should_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n' : ")
if should_play == 'y':
  play_game = True
else:
  play_game = False

while play_game:
  clear()
  print(logo)

  user_cards = [random.choice(cards), random.choice(cards)]
  computer_cards = [random.choice(cards), random.choice(cards)]
  computer_first_card = computer_cards[1]
  user_score = calculate_score(user_cards)
  computer_score = calculate_score(computer_cards)

  if user_score > 21:
    change_11_into_1(user_cards)
    user_score = calculate_score(user_cards)
            
  print(f"Your cards: {user_cards}, current score: {user_score}\nComputer's first card: {computer_first_card}")
  another_card = input("Type 'y' to get another card, type 'n' to pass: ")
  if another_card == 'y':
    should_restart = True
  elif another_card == 'n':
    should_restart = False
  
  while should_restart:
    user_cards.append(random.choice(cards))
    user_score = calculate_score(user_cards)
    if user_score > 21:
      if 11 in user_cards:
        change_11_into_1(user_cards)
      else:
        should_restart = False
        break
    else:
      print(f"Your cards: {user_cards}, current score: {user_score}\nComputer's first card: {computer_first_card}")
      another_card = input("Type 'y' to get another card, type 'n' to pass: ")
      if another_card == 'y':
        should_restart = True
      elif another_card == 'n':
        should_restart = False
  
  if computer_score < 17:
    computer_draws = True
  else:
    computer_draws = False
  
  while computer_draws:
    computer_cards.append(random.choice(cards))
    computer_score = calculate_score(computer_cards)
    if computer_score > 21:
      if 11 in computer_cards:
        change_11_into_1(computer_cards)
    if computer_score >= 17:
      computer_draws = False
  
  print(f"Your final hand: {user_cards}, final score: {user_score}\n Computer's final hand: {computer_cards}, final score: {computer_score}")
  
  if 21 > user_score > computer_score:
    print("You win!")
  elif user_score == 21:
    print("Win with a Blackjack!")
  elif 21 > computer_score > user_score:
    print("You lose.")
  elif computer_score == 21:
    print("Lose, opponent has a Blackjack.")
  elif user_score > 21:
    print("You went over. You lose.")
  elif computer_score > 21:
    print("Computer went over. You win!")
  elif user_score == computer_score:
    print("Draw.")

  should_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n' : ")
  if should_play != 'y':
    play_game = False