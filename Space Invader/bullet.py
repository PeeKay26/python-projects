import turtle

class Bullet(turtle.Turtle):
    def __init__(self):
        super().__init__()
        turtle.register_shape("space\missile.gif")
        self.color('yellow')
        self.speed(0)
        self.shape("space\missile.gif")
        self.pu()
        self.hideturtle()
        self.goto(0,-240)
        self.speedamt=22
        self.state="Ready"

# scr=turtle.Screen()
# scr.setup(1000, 700, 0, 0)
# B=Bullet()

# turtle.done()