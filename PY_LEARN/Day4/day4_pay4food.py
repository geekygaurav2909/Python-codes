import random

names = ['Angela', 'Ben', 'Jenny', 'Michael', 'Chloe']

lenArray = len(names) -1 

randomNames = names[random.randint(0,lenArray)]

print(randomNames)