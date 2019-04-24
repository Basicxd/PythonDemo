from sense_hat import SenseHat
from time import sleep
from random import randint

sense = SenseHat()
sense.clear()

blue = (0, 0, 255)
red = (255, 0, 0)
green = (0, 255, 0)
black = (0, 0, 0)
speedForRoation = 0.5

def red():
  sense.clear(255, 0, 0)

def blue():
  sense.clear(0, 0, 255)

def green():
  sense.clear(0, 255, 0)
  
def yellow():
  sense.clear(255, 255, 0)

sense.stick.direction_up = red
sense.stick.direction_down = blue
sense.stick.direction_left = green
sense.stick.direction_right = yellow
sense.stick.direction_middle = sense.clear 

while True:
  pass 
  
