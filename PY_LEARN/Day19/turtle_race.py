from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.title("Turtle Race") 
screen.setup(width= 500, height= 400)
colors = ['red','orange','blue','green','yellow']
y_index = [-132,-66,0,66,132]
all_turtle = []

def main():
    flag = True
    create_turtle()
    while flag:
        user_bet = screen.textinput(title="Make a guess",prompt= "Which turtle will win the race? Choose a color: ")
        winner = start_race(bet=user_bet)

        if winner == user_bet:
            should_continue = screen.textinput(title= f"You have won. Winner is {winner}", prompt="Do you want to play again, Type 'Yes' for yes, and 'no' for exit. ").lower()
            flag = replay(should_continue)
        else:
            should_continue = screen.textinput(title= f"You have lost. Winner is {winner}", prompt="Do you want to play again, Type 'Yes' for yes, and 'no' for exit. ").lower()
            flag = replay(should_continue)


def create_turtle():
    for turtle_index in range(0,5):
        new_turtle = Turtle(shape= 'turtle')
        new_turtle.penup()
        new_turtle.goto(x=-230,y=y_index[turtle_index])
        new_turtle.color(colors[turtle_index])
        all_turtle.append(new_turtle)


def start_race(bet):
    if bet:
        is_race_on = True

    while is_race_on:

        for turtle in all_turtle:
            if turtle.xcor()> 230:
                winning_color = turtle.pencolor()
                is_race_on = False               
            else:
                turtle.forward(random.randint(0,10))
        
    return winning_color

def replay(play_again):
    if play_again == 'yes':
        flag = True
        repeat_game()
    else:
        flag = False

    return flag

def repeat_game():
    for i, turtle_idx in enumerate(all_turtle):
        turtle_idx.goto(x= -230, y = y_index[i])


main()

    
screen.exitonclick()