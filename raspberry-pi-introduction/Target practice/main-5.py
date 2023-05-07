#!/bin/python3

# Import library code
from p5 import *
from random import randint

# The mouse_pressed function goes here
def mouse_pressed():
  print( hit_color.red, hit_color.green, hit_color.blue )
  if hit_color == outer:
    print('You hit the outer circle, 50 points!')
  elif hit_color == inner:
    print('You hit the inner circle, 200 points!')
  elif hit_color == middle:
    print('You hit the middle, 500 points!')
  else:
    print('You missed! No points!')

# The shoot_arrow function goes here
def shoot_arrow():
  global hit_color # Can be used in other functions
  arrow_x = randint(100, 300) # Store a random number between 100 and 300
  arrow_y = randint(100, 300) # Store a random number between 100 and 300
  
  load_pixels() # Makes the pixels variable available
  hit_color = pixels._get_pixel((arrow_x, arrow_y))

  fill(wood) # Set the arrow to fill colour to wood
  circle(arrow_x, arrow_y, 15) # Draw a small circle at random coordinates

def setup():
# Setup your game here
  size(400, 400) # width and height
  no_stroke()

# Things to do in every frame
def draw():
  global wood, outer, inner, middle
  sky = Color(92, 204, 206) # Red = 92, Green = 204, Blue = 206
  grass = Color(149, 212, 122)
  wood = Color(145, 96, 51)
  outer = Color(0, 120, 180)
  inner = Color(210, 60, 60) # Red
  middle = Color(220, 200, 0) # Yellow

  fill(sky)
  rect(0, 0, 400, 250)

  fill(grass) # Set the fill color to grass
  rect(0, 250, 400, 150) # x, y, width, height

  fill(wood) # Set the stand fill colour to wood
  triangle(150, 350, 200, 150, 250, 350)

  fill(outer) # Set the circle fill colour to outer
  circle(200, 200, 170) # x, y, width of the circle
  
  fill(inner) # Set the circle fill colour to inner
  circle(200, 200, 110) # Inner circle - x, y, width of the circle
  fill(middle) # Set the circle fill colour to middle
  circle(200, 200, 30) # Middle circle - x, y, width of the circle

  shoot_arrow()

# Keep this to run your code
run(frame_rate=2)