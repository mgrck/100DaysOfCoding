from replit import clear
from art import logo
print(logo)

bids = {}
again = True

# def finding_winner(bidding_record):
#   highest_bid = 0
#   winner = ''
#   for bidder in bidding_record:
#     if bidding_record[bidder] > highest_bid:
#       highest_bid = bidding_record[bidder]
#       winner = bidder
#   print(f"The winner is {winner} with a bid of ${highest_bid}")

def finding_winner():
  winner = max(bids, key=bids.get)
  max_bid = bids[winner]
  print(f"The winner is {winner} with a bid of ${max_bid}")

while again:
  name = input("What's your name?")
  bid_price = int(input("What's your bid? $"))
  bids[name] = bid_price
  another_bid = input("Are there any other bidders? Type 'yes' or 'no'.\n")
  if another_bid == 'yes':
    clear() 
  elif another_bid == 'no':
    again = False
    finding_winner(#bids)
    )
