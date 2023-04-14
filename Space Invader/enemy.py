import turtle, random

class Enemy(turtle.Turtle):
    def __init__(self):
        super().__init__()
        turtle.register_shape("space\enemy.gif")
        self.color('red')
        self.speed(0)
        self.shape("space\enemy.gif")
        self.pu()
        self.setheading(90)
        x=random.randint(-300,300)
        y=random.randint(180,260)
        self.goto(x,y)
        self.speedamt=5

# scr=turtle.Screen()
# scr.setup(1000, 700, 0, 0)
# E=Enemy()

# turtle.done()