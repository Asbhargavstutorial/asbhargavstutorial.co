from turtle import *

colors=['red','green','blue','yellow','orange','white']

bgcolor('black')

for x in range (360):
    pencolor(colors[x%6])
    width(x/100+1)
    forward(x)
    left(59)
    speed(15)
