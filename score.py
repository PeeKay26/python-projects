import turtle

class Score(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.pencolor("white")
        self.speed(0)
        self.ScoreValue=0
        self.pu()
        self.setposition(-355, 280)
        self.scorestr="Score: %s "%self.ScoreValue
        self.write(self.scorestr, False, align="left", font=("Arial",14,"normal"))
        self.hideturtle()