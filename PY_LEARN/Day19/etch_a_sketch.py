from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
input_list = ['W','S','A','D','C']

def move_fd():
    tim.fd(10)
    
def move_bk():
    tim.bk(10)

def move_right():
    tim.right(10)

def move_left():
    tim.left(10)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.onkeypress(fun=move_fd,key='W')
screen.onkeypress(fun=move_bk,key='S')
screen.onkeypress(fun=move_left,key='A')
screen.onkeypress(fun=move_right,key='D')
screen.onkeypress(fun=clear,key='C')

screen.listen()

screen.exitonclick()