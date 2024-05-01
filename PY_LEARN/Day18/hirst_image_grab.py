# import colorgram

# colors = colorgram.extract('images.jpg',2 ** 32)
# color_code = []

# for index_pos in colors:
#     r = index_pos.rgb.r
#     g = index_pos.rgb.g
#     b = index_pos.rgb.b
#     final_code = (r,g,b)
#     color_code.append(final_code)

# print(color_code)

import turtle as t
import random

tim = t.Turtle()

t.colormode(255)
tim.speed("fastest")
tim.penup()
tim.setpos(-250.00,-200.00)
tim.hideturtle()

color_list = [(202, 168, 124), (138, 116, 23), (174, 145, 39), (225, 228, 232), (198, 201, 133), (231, 225, 228), (65, 109, 144), (5, 31, 64), (66, 129, 126), (98, 68, 76), (217, 145, 150), (122, 31, 11), (202, 89, 93), (218, 203, 30), (4, 87, 83), (90, 30, 21), (90, 42, 44), (2, 84, 87), (198, 92, 89), (80, 36, 38), (142, 164, 178), (137, 170, 160), (5, 69, 61), (94, 144, 133), (222, 180, 167), (68, 102, 14), (225, 169, 173), (175, 204, 188), (99, 130, 161), (99, 139, 143), (45, 61, 87), (183, 190, 203), (173, 200, 205)]

def dot_move():
    for _ in range(10):
        tim.dot(20, random.choice(color_list))
        tim.fd(50)

for _ in range(10):
    dot_move()
    tim.left(90)
    tim.fd(50)
    tim.left(90)
    tim.fd(500)
    tim.right(180)

screen = t.Screen()
screen.exitonclick()