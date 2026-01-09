from turtle import Turtle
# Class for level

class Level(Turtle):
    def __init__(self):
        super().__init__()
        self.player_level = 1
        self.hideturtle()
        self.penup()
        self.color("black")
        self.goto(x=-280, y=260)
        self.write_level()


    def increment_level(self):
        self.player_level += 1
        self.write_level()

    def write_level(self):
        self.clear()
        self.write(
            arg=f"Level: {self.player_level}",
            align= "left",
            move=False,
            font= ("Arial", 20, "italic")
        )