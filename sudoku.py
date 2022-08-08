import freegames
import random
import turtle

tiles={}
neighbors=[freegames.vector(100,0),
freegames.vector(-100,0),
freegames.vector(0,100),
freegames.vector(0,-100)
]

def load():
  count=1
  for y in range(-200,200,100):
    for x in range(-200,200,100):
      mark=freegames.vector(x,y)
      print(mark)
      tiles[mark]=count
      count+=1
  tiles[mark]=None
  print(tiles)

  for count in range(1000):
    neighbor=random.choice(neighbors)
    spot=mark+neighbor

    if spot in tiles:
      number=tiles[spot]
      tiles[spot]=None
      tiles[mark]=number
      mark=spot

def square(mark,number):
  t.pu()
  t.goto(mark.x, mark.y)
  t.pd()
  t.color('black','white')
  t.begin_fill()
  for count in range(4):
    t.forward(90)
    t.left(90)
  t.end_fill()
  #t.write(number,font=("Arial",60,"normal"))

  if number is None:
    return
  elif number<10:
    t.forward(20)

  t.write(number,font=('Arial',55,'normal'))

def tap(x,y):
  x=freegames.floor(x,100)
  y=freegames.floor(y,100)
  mark=freegames.vector(x,y)
  
  for neighbor in neighbors:
    spot = mark+neighbor

    if spot in tiles and tiles[spot] is None:
      number = tiles[mark]
      tiles[spot] = number
      square(spot, number)
      tiles[mark] = None
      square(mark,None)


def draw():
  for mark in tiles:
    square(mark, tiles[mark])
  turtle.update()

turtle.setup(420,420)
turtle.ht()
turtle.tracer(False)
t=turtle.Turtle()
t.hideturtle
load()
draw()
turtle.onscreenclick(tap)

turtle.done()
