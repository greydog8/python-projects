from turtle import Turtle
from random import random
bob= Turtle()
def random_color():
    return (random(),random(),random())

bob.pensize(10)

for count in range(5000):
    bob.color(random_color())
    bob.forward(100)
    bob.left(182)
