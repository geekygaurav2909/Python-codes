import turtle as t
import random

tim = t.Turtle()
# Draw a square
# for _ in range(4):
#     tim.fd(100)
#     tim.left(90)

# Draw a dashed line
# for _ in range(10):
#     tim.fd(10)
#     tim.up()
#     tim.fd(10)
#     tim.down()

# Draw multiple shapes - Triangle, Square, Pentagon, Hexagon, Heptagon, Octagon, Nonagon, Decagon
# colors= ['red','GreenYellow','black','indigo','Yellow','tomato']

# def draw_patterns(sides):
#     angle = 360/sides
#     for _ in range(sides):
#         tim.right(angle)
#         tim.fd(100)

# for shape_size in range(3,11):
#     tim.color(random.choice(colors))
#     draw_patterns(shape_size)

# Random walk
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    my_tuple = (r, g, b)
    return my_tuple

tim.speed("fastest")
# move = [0,90,180,270]

# 
# tim.pensize(7)

# for _ in range(200):
#     tim.color(random_color())
#     tim.fd(30)
#     tim.setheading(random.choice(move))
    
# Exercise - 5: Draw a Spirograph
# Way -1
# for _ in range(72):
#     tim.color(random_color())
#     tim.circle(100)
#     tim.left(5)

# Way-2

# def draw_spirograph(size_of_gap):
#     for _ in range(int(360/size_of_gap)):
#         tim.color(random_color())
#         tim.setheading(tim.heading() + size_of_gap)
#         tim.circle(100)


# draw_spirograph(20)



screen = t.Screen()
screen.exitonclick()