import os
import random
from blackjack_art import logo
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
play_again = True

def deal_card():
        return random.choice(cards) # helps in returning more than two random value at a time

def calculate_score(card_list):
    score = sum(card_list)
    if 11 in card_list and score> 21:
        card_list.remove(11)
        card_list.append(1)
        score = sum(card_list)
    return score


while play_again:
    print("Welcome to my BlackJack Project!")
    print(logo)

    user_cards = []
    computer_cards = []

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    # user_cards = [deal_card(), deal_card()]
    # computer_cards = [deal_card(), deal_card()]

    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)

    print(f"  Your cards: {user_cards}, current score: {user_score}") 
    print(f"  Computer's first card: {computer_cards[0]}") 

    while user_score < 21:
        another_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        if another_card == 'y':
            user_cards.append(deal_card())
            user_score = calculate_score(user_cards)
            print(f"  Your cards: {user_cards}, and current score: {user_score}")
            print(f"  Computer's first card: {computer_cards[0]}")
        else:
            break;
        
    while computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"  Your cards: {user_cards}, final score: {user_score}")
    print(f"  Computer's final hand: {computer_cards} and final score: {computer_score}")

    if user_score > 21:
        print("  You went over. You lose😒")
    elif computer_score < user_score or computer_score > 21:
        print("  You win 😂")
    elif user_score < computer_score:
        print("  You lose.😒")
    else:
        print("  It's a draw 👍")

    play_again_input = input("Do you want to play again? Type 'y' for yes. Otherwise 'n' for no.: ").lower()
    if play_again_input != 'y':
        play_again = False
    else:
        os.system('cls' if os.name == 'nt' else 'clear')