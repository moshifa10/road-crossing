from turtle import Turtle,Screen
import random
import time
# In this class I will be creating cars and move at the specific pace

class Cars(Turtle):
    def __init__(self):
        super().__init__(shape="square")
        self.screen.colormode(255)
        self.penup()
        self.setheading(180)
        self.decrement = 5
        self.x_cor = 290
        self.y_cor = random.randint(-280, 280)
        self.goto(x=290, y=self.y_cor)
        self.shapesize(stretch_len=2, stretch_wid=1)
        self.color(self.create_color())

    def create_color(self):
        return (random.randint(0,255), random.randint(0,255),random.randint(0,255))
    
    def increment(self):
        self.decrement += 5

    def move(self):
        self.x_cor -= self.decrement
        self.goto(x=self.x_cor, y=self.y_cor)