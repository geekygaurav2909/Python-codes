from turtle import Turtle
LOCATION = (0,260)
POSITION = 'center'
FONT_CHAR = ('Arial',14,'normal')

with open("highscore.txt",mode="r+") as file:
    h_score = int(file.read())
    print(f"The value is: {h_score}")

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = h_score
        self.ht()
        self.penup()
        self.color('white')
        self.goto(LOCATION)
        self.update_score()    


    def update_score(self):
        self.clear()
        self.write(f'Your score: {self.score} High Score: {self.high_score}', align=POSITION, font=FONT_CHAR)


    # def game_over(self):
    #     self.goto(0,0)
    #     self.write('GAME OVER!', align=POSITION, font=FONT_CHAR)
        

    def reset_game(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("highscore.txt","w+") as writemode:
                h_score = writemode.write(str(self.high_score))
        self.score = 0
        self.update_score()

    
    def score_update(self):
        self.score += 1
        self.update_score()

        