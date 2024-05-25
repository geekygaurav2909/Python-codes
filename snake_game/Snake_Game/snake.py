from turtle import Turtle
POSITION = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
DOWN = 270
LEFT = 180
UP = 90
RIGHT = 0


class Snake:

    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):
        for pos in POSITION:
            self.add_snake(pos)

    def add_snake(self, position):
        snake = Turtle(shape= "square")
        snake.penup()
        snake.color("white")
        snake.goto(position)
        self.snake_body.append(snake)


    def reset_snake(self):
        for body in self.snake_body:
            body.goto(1000,1000)
        self.snake_body.clear()
        self.create_snake()
        self.head = self.snake_body[0]



    def extend_body(self):
        #extend body
        self.add_snake(position=self.snake_body[-1].position())


    def move(self):
        for snake_idx in range(len(self.snake_body)-1,0,-1):
            new_x = self.snake_body[snake_idx -1].xcor()
            new_y = self.snake_body[snake_idx -1].ycor()
            self.snake_body[snake_idx].goto(new_x,new_y)
    
        self.head.fd(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)