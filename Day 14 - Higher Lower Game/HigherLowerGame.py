from game_data import data
from art import logo, vs
import random
from replit import clear

def format_data(account):
  name = account['name']
  description = account["description"]
  country = account["country"]
  return f"{name}, {description}, from {country}."

def get_followers(account):
  return account['follower_count']

should_restart = True
score = 0

account_a = random.choice(data)
followers_a = get_followers(account_a)

while should_restart:
  print(logo)
  if score != 0:
    print(f"You're right! Current score: {score}")
  
  print(f"Compare A: {format_data(account_a)}.")
  
  print(vs)
  
  account_b = random.choice(data)
  followers_b = get_followers(account_b)
  print(f"Against B: {format_data(account_b)}.")
  answer = input("Who has more followers? Type 'A' or 'B': ").lower()
  
  correct_answer = ""
  if followers_a > followers_b:
    correct_answer = 'a'
  elif followers_a < followers_b:
    correct_answer = 'b'
  elif followers_a == followers_b:
    correct_answer = answer

  if correct_answer == answer:
    score += 1
    account_a = account_b
    clear()
  else:
    should_restart = False
    clear()

print(logo)
print(f"Sorry that's wrong. Final score: {score}")
