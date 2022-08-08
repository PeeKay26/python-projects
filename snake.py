import turtle
import time
import random

delay = 0.2
score = 0
highscore= 0

win=turtle.Screen()
win.title("Snake Game")
win.bgcolor("light blue")
win.setup(width = 800, height = 600)

head = turtle.Turtle()
head.shape("square")
head.penup()
head.color("green")
head.direction = "Stop"

food=turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0,100)

sc=turtle.Turtle()
sc.speed(0)
sc.shape("square")
sc.color("white")
sc.penup()
sc.hideturtle()
sc.goto(0,250)
sc.write("Score: 0 High Score: 0", align='center', font=('candara',24, 'bold'))

def up():
  if head.direction!='down':
    head.direction='up'
def down():
  if head.direction!='up':
    head.direction='down'
def left():
  if head.direction!='right':
    head.direction='left'
def right():
  if head.direction!='left':
    head.direction='right'
  
def move():
  if head.direction == 'up':
    y=head.ycor()
    head.sety(y+20)
  if head.direction == 'down':
    y=head.ycor()
    head.sety(y-20)
  if head.direction == 'left':
    x=head.xcor()
    head.setx(x-20)
  if head.direction == 'right':
    x=head.xcor()
    head.setx(x+20)

win.listen()
win.onkeypress(up,'w')
win.onkeypress(down,'s')
win.onkeypress(left,'a')
win.onkeypress(right,'d')

segments=[]

while True:
  win.update()
  if (head.xcor()>390) or (head.xcor()< -390) or     (head.ycor()>290) or (head.ycor()< -290):
    time.sleep(1)
    head.goto(0,0)
    head.direction='Stop'

    for segment in segments:
      segment.goto(1000,1000)
    segments.clear()
    score=0
    delay=0.2
    sc.clear()
    sc.write("Score: {} High Score: {}".format(score,highscore), align='center', font=('candara', 24,'bold'))

  if head.distance(food)<20:
    x=random.randint(-370,370)
    y=random.randint(-270,270)
    food.goto(x,y)

    new_segment = turtle.Turtle()
    new_segment.speed(0)
    new_segment.color("orange")
    new_segment.penup()
    new_segment.shape("square")
    segments.append(new_segment)

    delay = delay-0.002

    score +=1
    if score>highscore:
      highscore=score
    sc.clear()
    sc.write("Score: {} High Score: {}".format(score,highscore), align='center', font=('candara', 24,'bold'))

  for index in range(len(segments)-1,0,-1):
    x=segments[index-1].xcor()
    y=segments[index-1].ycor()
    segments[index].goto(x,y)

  if len(segments)>0:
    x=head.xcor()
    y=head.ycor()
    segments[0].goto(x,y)
  
  move()

  for segment in segments:
      if segment.distance(head)<10:
        time.sleep(1)
        head.goto(0,0)
        head.direction="Stop"

        for segment in segments:
          segment.goto(1000,1000)
        segments.clear()

        score = 0
        delay = 0.1

        sc.clear()
        sc.write("Score: {} High Score: {}".format(score,highscore), align='center', font=('candara', 24,'bold'))
        
  time.sleep(delay)

turtle.done()
