from turtle import Turtle

# Here I will be creating an object of a turtle

class Player(Turtle):
    def __init__(self):
        super().__init__(shape="turtle")
        self.x_cor = 0
        self.y_cor = -280
        self.color("black")
        self.setheading(90)
        self.penup()
        self.move()


    def move(self):
        # if not (self.x_cor > 290 or self.x_cor < -290):
        self.goto(x=self.x_cor, y=self.y_cor)
        # else:
            # self.x_cor -= 20
    # How it moves
    def up(self):
        self.y_cor += 20

    def go_left(self):
        self.x_cor -= 20
    
    def go_right(self):
        self.x_cor += 20