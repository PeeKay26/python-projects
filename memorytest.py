import freegames
import turtle
import random
import time

pattern = []
guesses = []
tiles = {
  freegames.vector(0,0):('red','dark red'),
  freegames.vector(0,-200):('cyan','sky blue'),
  freegames.vector(-200,0):('light green','green'),
  freegames.vector(-200,-200):('yellow','gold')
}
def grid():
  freegames.square(0,0,200,'dark red')
  freegames.square(0,-200,200,'sky blue')
  freegames.square(-200,0,200,'green')
  freegames.square(-200,-200,200,'gold')

def flash(tile):
  glow, dark=tiles[tile]
  freegames.square(tile.x, tile.y,200, glow)
  turtle.update()
  time.sleep(0.5)
  freegames.square(tile.x,tile.y,200, dark)
  turtle.update()
  time.sleep(0.5)

def grow():
  tile=random.choice(list(tiles))
  pattern.append(tile)
  for tile in pattern:
    flash(tile)

  guesses.clear()

def tap(x,y):
  scr.onscreenclick(None)
  x=freegames.floor(x, 200)
  y=freegames.floor(y,200)
  tile=freegames.vector(x,y)
  index=len(guesses)
  if tile!=pattern[index]:
    exit()
  guesses.append(tile)
  flash(tile)

  if len(guesses)==len(pattern):
    grow()

  scr.onscreenclick(tap)

scr=turtle.Screen()
scr.tracer(False)
grid()
grow()
scr.onscreenclick(tap)
