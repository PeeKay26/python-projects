import turtle, winsound, math, random
from glob import glob
from player import Player
from bullet import Bullet
from enemy import Enemy 
from score import Score

# setting up the screen
scr=turtle.Screen()
scr.setup(800, 650, 0, 0)
scr.bgcolor("black")
scr.title("Space War")
scr.bgpic("space\dp.gif")
# turtle.register_shape("\space\player.gif")
# turtle.register_shape("space\enemy.gif")
# turtle.register_shape("space\missile.gif")

p=Player()
enemies=[]
for i in range(6): #no of enemies
    enemies.append(Enemy())

b= Bullet()
sc=Score()

def collisionplay(a,b):
    distance=math.sqrt(abs(math.pow((a.xcor()-b.xcor()),2)+math.pow((a.ycor()-b.ycor()),2)))
    if distance<25:
        return True
    else:
        return False

def collision(a,b):
    distance=math.sqrt(abs(math.pow((a.xcor()-b.xcor()),2)+math.pow((a.ycor()-b.ycor()),2)))
    if distance<20:
        return True
    else:
        return False

def fireBullet():
    global selfstate
    if b.state=="Ready":
        b.state="Fire"
        # winsound.PlaySound("space\laser.wav")
        x=p.xcor()
        y=p.ycor()+10
        b.goto(x,y)
        b.showturtle()


# key bindings
turtle.listen()
turtle.onkey(p.move_left,"Left")
turtle.onkey(p.move_right,"Right")
turtle.onkey(fireBullet,"space")

#main loop
while True:
    for enemy in enemies:
        x=enemy.xcor()
        x+=enemy.speedamt
        enemy.setx(x)
        # movement back and down
        if enemy.xcor()>325:
            for j in enemies:
                y=j.ycor()
                y-=25 #enemy speed
                j.sety(y)
            enemy.speedamt*=-1
        if enemy.xcor()<-325:
            for j in enemies:
                y=j.ycor()
                y-=15
                j.sety(y)
            enemy.speedamt*=-1

        #check for collision
        if collisionplay(b,enemy):
            b.hideturtle()
            b.state="Ready"
            b.setposition(0,-400)
            x=random.randint(-300, 300)
            y = random.randint(180,280)
            enemy.setposition(x,y)
            #score
            sc.ScoreValue+=10
            sc.scorestr="Score: %s "%sc.ScoreValue
            sc.clear()
            sc.write(sc.scorestr, False, align="left", font=("Arial",14,"normal"))

        if collision(p,enemy):
            for e in enemies:
                e.hideturtle()
            p.hideturtle()
            #score
            sc.pu()
            sc.goto(0,0)
            sc.pd()
            sc.write("Game Over", False, align="left", font=("Arial",14,"normal"))
            sc.pu()
            sc.setposition(-355,200)

            break

        if enemy.ycor()<=-200:
            for j in enemies:
                j.hideturtle()
            p.hideturtle()
            #score
            sc.pu()
            sc.goto(0,0)
            sc.pd()
            sc.write("Game Over", False, align="left", font=("Arial",14,"normal"))
            sc.pu()
            sc.setposition(-355,200)

            break

    #bullet movenment 
    y=b.ycor()
    y+=b.speedamt
    b.sety(y)

    if b.ycor()>150:
        b.state='Ready'

    if b.ycor()>300:
        b.hideturtle()
        b.state="Ready"

delay=input()