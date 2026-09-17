import turtle
from turtle import *
t = Turtle()
t.shape('turtle')

def square(x):
     y= 10
     for i in range(5):
        t.forward(100)
        t.left(50)
        print(i)
        y-=1
        square(100)
square(100)

