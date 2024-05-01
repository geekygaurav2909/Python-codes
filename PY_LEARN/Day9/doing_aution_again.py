def find_highest_bidder(bidder_rec):
    # {"Gaurav": 123, "Anjula": 321}
    highest_amount = 0
    winner = ""
    for bidder in bidder_rec:
        bid_amount = bidder_rec[bidder]
        if bid_amount > highest_amount:
            highest_amount = bid_amount
            winner = bidder
    print(f"The winner name is {winner} with a bidding value of {highest_amount}")

import os
from blind_auction_art import logo
print(logo)
print("Welcome to my first auction program.")
bidder_available = True
while bidder_available:
    bids = {}
    name = input("What's your name?: ")
    price = int(input("What is your bidding price?: $ "))
    bids[name] = price

    other_available_bidder = input("Are there other bidder available? Type 'Yes' or 'no'.").lower()
    if other_available_bidder == 'no':
        bidder_available = False
        find_highest_bidder(bids)
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
