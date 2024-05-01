
bidder_dict = {}

def highest_bidder_finder(bidding_rec):
    print(bidding_rec)
    highest_bidder = 0
    winner = ""

    for detail in bidding_rec:
        bid_amount = bidding_rec[detail]
        if bid_amount> highest_bidder:
            highest_bidder = bid_amount
            winner = detail
    print(f"The winner is {winner} with a bid of ${highest_bidder}")

import os
from blind_auction_art import logo
print(logo)
print("Welcome to the secret auction program.")

bidder_available = True
while bidder_available:
    bidder_name = input("What is your name?: ")
    bidder_price = int(input("What is your bidding price?:$ "))
    bidder_dict[bidder_name] = bidder_price

    other_bidder_available = input("Are there any other bidders? Type 'Yes' or 'no'.").lower()
    if other_bidder_available == "no":
        bidder_available = False
        highest_bidder_finder(bidder_dict)
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
