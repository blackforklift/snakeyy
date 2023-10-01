from turtle import Turtle
TEXT_ALIGNMENT='center'
FONT=('Arial', 18, 'normal')
class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.setpos(0, 270)
        self.hideturtle()
        self.printScore()
    def printScore(self):
        self.write(f"score: {self.score}", move=False, align=TEXT_ALIGNMENT, font=FONT)
    def updateScore(self):
        self.score +=1
        self.clear()
        self.printScore()

    def game_over(self):
        self.home()
        self.write(f"GAME OVER", move=False, align=TEXT_ALIGNMENT, font=FONT)
