print('''
                     .---.
        .--.     ___/     |
       /    `.-""   `-,    ;
      ;     /     O O  \  /
      `.    \          /-'
     _  J-.__;      _.'
    (" /      `.   -=:
     `:         `, -=|
      |  F\    i, ; -|
      |  | |   ||  \_J
 fsc  mmm! `mmM Mmm'
      ''')

print("Welcome to the Elephant riddle game!\n")
print("Your mission is find the elephant..\n \nLet's start your journey in the Jungle \n")

takeTurn = input("Where your want to head for? type R for Right or L for left: ").lower()

if takeTurn != 'l':
    print("Opps! You fallen into a well. Game Over!! try again")
elif takeTurn == 'l':
    swimWait = input("Do you want to swim or wait? Type S for Swim or W for Wait: ").lower()
    if swimWait != 'w':
      print("Oh! Again, you could have waited, The river is quite deep \n Game Over!!")
    else:
       print("Great! You have reached to a final steps. Be Aware with your decision \n")
       chooseDoor = input("We have three doors, choose only one door wisely. Type Y for Yellow, R for Red, B for Blue.").lower()
       if chooseDoor == 'y':
          print("Great! You have find the elephants! Thanks you champ! You Win!!")
       elif chooseDoor == 'r':
          print("Oh, Fire inside, You were burnt. Game Over!!")
       elif chooseDoor == 'b':
          print("Eaten by Beast! Game Over")
       else:
          print("Game Over")
          

          
       





# else:
#     
#     chooseDoor = input("We have three doors, choose only one door wisely. Type Y for Yellow, R for Red, B for Blue.")

# if chooseDoor.lower() == 'y':
#     print("Great! You have find the elephants! Thanks you champ! You Win!!")
# elif chooseDoor.lower() == 'r':
#     print("Oh, Fire inside, You were burnt. Game Over!!")
# elif chooseDoor.lower() == 'b':
#     print("Eaten by Beast! Game Over")
# else:
#     print("Game Over")
          


