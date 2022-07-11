from turtle import *
from math import *
from random import *

def figure(n, color, R=40):
  a= 2*R*sin(pi/n)
  penup()
  left((180 + 360/n)/2)
  forward(R)
  setheading(0)
  pendown()
  fillcolor(color)
  begin_fill()
  for _ in range(n):
    forward(a)
    right(180 - 180*(n-2)/n)
  end_fill()

speed(0)
R = 30
t = 4*R + 20
step = 2*R + 10
for i in range(-t, t + 1, step):
  for j in range(t, -t - 1, -step):
    penup()
    goto(i,j)
    color = 'white'
    figure(randint(3,10), color, R)