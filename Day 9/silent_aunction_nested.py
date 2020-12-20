#Nesting dictionaries in a list

from replit import clear
import art
print(art.logo)

bid_on = True
auction_list = []
bid_dict = {}

def highest_bid():
  winning_bid = auction_list[0]["bid_price"] 
  winning_name = auction_list[0]["name"] 
  for value in range(len(auction_list)):
    check = auction_list[value]["bid_price"] 
    name_check = auction_list[value]["name"] 
    if check > winning_bid:
      winning_bid = check
      winning_name = name_check
  print(f"The winner of the bid is {winning_name} with {winning_bid}")

while bid_on:

  name = input("What is your name?\n").lower()
  bid_price = int(input("Please enter your bid price $\n"))

  bid_dict['name'] = name
  bid_dict["bid_price"] = bid_price
  auction_list.append(bid_dict)
  
  new_request = input("Are there are other users that want to bid ?")
  clear()
  if new_request == "yes":
      bid_on = True
  else:
      bid_on = False
      highest_bid()
