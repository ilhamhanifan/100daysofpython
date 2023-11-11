# First-price sealed-bid auction

from art import logo
import os

def find_highest_bidder(bid_records):
    highest_bid = 0
    winner = ""

    for bidder in bid_records:
        if bids[bidder] > highest_bid:
            winner = bidder
            highest_bid = bids[bidder]
    return [winner, highest_bid]
    
os.system('clear')

bids = {}

play = True
while play:
    print(logo)
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: "))
    userinput = input("Are there any other bidders? type 'yes' or 'no'.\n")
    bids[name] = bid
    os.system('clear')
    if userinput == "no":
        play = False

winner, highest_bid = find_highest_bidder(bids)
print(f"The winner is {winner} with a bid of ${highest_bid}")
