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

game_images = [rock,paper,scissors]
images_text = ["Rock", "Paper", "Scissors"]
userInput = int(input("What do you choose? Type 0 for Rock, 1 for Paper, 2 for Scissors. \n"))

if userInput > 2 or userInput < 0:
    print("Wrong Input, You lose")
else:
    print(f"You choose: {userInput} or {images_text[userInput]}")
    print(game_images[userInput])
    computerInput = random.randint(0,2)

    print(f"Computer choose: {images_text[computerInput]}")
    print(game_images[computerInput])

    if computerInput == 0 and userInput == 2:
        print("You lose")
    elif computerInput ==2 and userInput == 0:
        print("You win")
    elif userInput > computerInput:
        print("You win")
    elif computerInput > userInput:
        print("You lose")
    elif userInput == computerInput:
        print("Match Draw")