
import pgzrun
import random

HEIGHT = 500
WIDTH = 900

players = []

gameover = False
winner = 0
y = 100
lineY = 150

def makeSwimmer():
  global y
  for i in range(4):
    swimmer = Actor("swimmingimg")
    swimmer.pos = (100,y)
    y += 100
    players.append(swimmer)

def moveSwimmers():
  for swimmer in players:
    distance = random.randint(1,3)
    swimmer.x = swimmer.x + distance

def draw():
  global players, winner, gameover, lineY
  screen.fill(color = "light blue")
  screen.blit("olympic",(350,10))
  screen.draw.line((0,lineY),(900,lineY), "red")
  winner = 1
  for swimmer in players:
    swimmer.draw()
    lineY += 100
    if swimmer.x >= 750:
      gameover = True
    else:
      moveSwimmers()
    winner += 1
  if gameover:
    screen.draw.text("Gamover! Player {} has won the race!".format(winner), center = (300,200), color = "white", fontsize = 30)


def update():
  pass

makeSwimmer()
pgzrun.go()