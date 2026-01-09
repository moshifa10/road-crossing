from turtle import Turtle,Screen
import random
import time
# In this class I will be creating cars and move at the specific pace
screen = Screen()
screen.colormode(255)
class Cars():
    def __init__(self,level):
        self.all_cars = []
        self.decrement = 5
        self.creat_player(level)
        

    def create_color(self):
        return (random.randint(0,255), random.randint(0,255),random.randint(0,255))
    
    def increment(self):
        self.decrement += 5

    def move(self, player:Turtle):
        x_cor, y_cor = player.pos()
        player.goto(x=x_cor - self.decrement, y=y_cor)

    def creat_player(self, level):
        for _ in range(level):
            car = Turtle(shape="square")
            car.speed(0)
            car.penup()
            car.setheading(180)
            x_cor = random.randint(-100, 10000)
            y_cor = random.randint(-240, 280)
            car.goto(x=x_cor, y=y_cor)
            car.shapesize(stretch_len=2, stretch_wid=1)
            car.color(self.create_color())
            self.all_cars.append(car)
        