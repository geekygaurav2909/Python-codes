import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

userInput = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors. \n"))

if userInput > 2 or userInput <0:
    print("Oops! Wrong input. You lose")
else:
    print(game_images[userInput])

    computerInput = random.randint(0,2)
    print(f"Computer choose: \n",game_images[computerInput])



    if userInput == 0 and computerInput == 2:
        print("You win")
    elif userInput ==2 and computerInput == 0:
        print ("you lose")
    elif userInput == computerInput:
        print("Match draw")
    elif (userInput > computerInput):
        print("You win")
    elif userInput < computerInput:
        print("You lose")
