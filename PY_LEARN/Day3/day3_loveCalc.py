print("The Love Calculator is calculating your score...")
name1 = input("What is your name? ") # What is your name?
name2 = input("What is their name? ") # What is their name?
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

trueCounter = 0
loveCounter = 0

partners = (name1 + name2).lower()

t_let = partners.count("t")
trueCounter += t_let
r_let = partners.count("r")
trueCounter +=r_let
u_let = partners.count("u")
trueCounter += u_let
e_let = partners.count("e")
trueCounter += e_let

l_let = partners.count("l")
loveCounter += l_let
o_let = partners.count("o")
loveCounter += o_let
v_let = partners.count("v")
loveCounter += v_let
ee_let = partners.count("e")
loveCounter += ee_let

total_numbers = int(str(trueCounter) + str(loveCounter))

if total_numbers < 10 or total_numbers > 90:
  print(f"Your score is {total_numbers}, you go together like coke and mentos.")
elif total_numbers >= 40 and total_numbers <= 50:
  print(f"Your score is {total_numbers}, you are alright together.")
else:
  print(f"Your score is {total_numbers}.")