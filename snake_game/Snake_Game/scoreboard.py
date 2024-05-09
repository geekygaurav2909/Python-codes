from turtle import Turtle
LOCATION = (0,260)
POSITION = 'center'
FONT_CHAR = ('Arial',14,'normal')


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.ht()
        self.penup()
        self.color('white')
        self.goto(LOCATION)
        self.update_score()    


    def update_score(self):
        self.write(f'Your score: {self.score}', align=POSITION, font=FONT_CHAR)


    def game_over(self):
        self.goto(0,0)
        self.write('GAME OVER!', align=POSITION, font=FONT_CHAR)

    
    def score_update(self):
        self.score += 1
        self.clear()
        self.update_score()

        