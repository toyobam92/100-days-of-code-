bids ={}
game_on = True

def highest_bid():
  highest_bid = 0
  winner = ""
  for bidders in bids:
        winning_bid = bids[bidders]
        if winning_bid > highest_bid:
          highest_bid = winning_bid
          winner = bidders
  print(f"The winning bid is {highest_bid} and the winner is {winner}")

while game_on :
  name = input("What is your name?")
  bid_price = int(input("Please enter your bid price?"))
  bids[name] = bid_price
  new_user_request = input("Will any other user like to bid?")       
  if new_user_request == "yes":
      game_on = True   
  else:
      game_on = False
      highest_bid()
