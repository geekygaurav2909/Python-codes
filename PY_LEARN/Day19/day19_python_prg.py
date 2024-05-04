from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_down():
    tim.back(20)

screen.listen()
screen.onkey(fun=move_down,key="space")

screen.exitonclick()