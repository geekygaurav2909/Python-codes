enemies = 1

def increase_enemies():
    enemies = 2
    print(f"The enemies inside the function: {enemies}")

increase_enemies()
print(f"The enemies outside the function : {enemies}")