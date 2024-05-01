line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?
# 🚨 Don't change the code above 👆
# Write your code below this row 👇

print(map)

A1 = map[0][0]
B1 = map[0][1]
C1 = map[0][2]
A2 = map[1][0]
B2 = map[1][1]
C2 = map[1][2]
A3 = map[2][0]
B3 = map[2][1]
C3 = map[2][2]

if position == "A1":
    map[0][0] = "X"
elif position == "B1":
    map[0][1] = "X" 
elif position == "C1":
    map[0][2] = "X" 
elif position == "A2":
    map[1][0] = "X" 
elif position == "B2":
    map[1][1] = "X" 
elif position == "C2":
    map[1][2] = "X"
elif position == "A3":
    map[2][0] = "X" 
elif position == "B3":
    map[2][1] = "X" 
elif position == "C3":
    map[2][2] = "X"
else:
    print('Invalid Input')


print("\n\n", position)


# Write your code above this row 👆
# 🚨 Don't change the code below 👇
print(f"{line1}\n{line2}\n{line3}")