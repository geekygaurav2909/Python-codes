from art_guess_the_number import logo
import random

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

random_number = random.randint(1,100)
print(f"Pssst, the correct answer is {random_number}")

life_point = {}

life_point["easy"] = 10
life_point["hard"] = 5

def life_available(chosen_level):
    ''' Function returns the number of life granted for chosen difficulty level'''
    return life_point[chosen_level]

while True:
    difficulty_level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty_level in ("easy","hard"):
        break;
    else:
        print("Please enter valid difficulty level")

chances = life_available(difficulty_level)
print(f"You have {chances} attempts remaining to guess the number.")

chances_available = chances
while chances_available > 0:
    guess_number = int(input("Make a guess: "))
    chances_available -=1

    if guess_number > random_number:
        print("Too High.")
    elif guess_number < random_number:
        print("Too Low.")
    else:
        print(f"You have guessed it right. The answer is {random_number}")
        break


    if guess_number != random_number and chances_available != 0:
        print(f"You have {chances_available} attempts remaining to guess the number.")

    if chances_available == 0:
        print(f"You've consumed all your {chances} chances. You lost")