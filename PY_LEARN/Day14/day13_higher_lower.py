from day13_higher_lower_art import logo,vs
from day13_game_data import data
import random
import os

# Pick up a random number from the list and fetch data from game_data.
def winner_finder(guess, compare_a, against_b):
    """Takes input as Guess and numbers and return who has won it"""
    if compare_a > against_b:
        return guess == 'a'
    else:
        return guess == 'b'

print(logo)    
final_counter = 0
play_should_continue = True
against_data = random.choice(data)

while play_should_continue:
    compare_data = against_data
    against_data = random.choice(data)
    
    if compare_data == against_data:
        against_data = random.choice(data)

    follower_a = compare_data["follower_count"]
    follower_b = against_data["follower_count"]

    print(f"A : {follower_a}")
    print(f"B : {follower_b}")

    print(f"Compare A: {compare_data["name"]}, a {compare_data["description"]}, from {compare_data['country']}")

    print(vs)

    print(f"Against B: {against_data["name"]}, a {against_data["description"]}, from {against_data['country']}")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()
    is_correct = winner_finder(guess, follower_a,follower_b)

    os.system('cls' if os.name == 'nt' else 'clear')
    print(logo)

    if is_correct:
        final_counter += 1
        print(f"You got is right, current score: {final_counter}")
    else:
        play_should_continue = False
        print(f"Sorry, That's wrong. Final score: {final_counter}")


