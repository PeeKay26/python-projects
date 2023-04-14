import turtle

class Player(turtle.Turtle):
    def __init__(self):
        super().__init__()
        turtle.register_shape("space\player.gif")
        self.color('green')
        self.speed(0)
        self.shape("space\player.gif")
        self.pu()
        self.goto(0,-250)

        self.playerspeed=40

    def move_left(self):
        x=self.xcor()
        x -= self.playerspeed
        if x < -340:
            x = -340
        self.setx(x)

    def move_right(self):
        x=self.xcor()
        x += self.playerspeed
        if x > 340:
            x = 340
        self.setx(x)

