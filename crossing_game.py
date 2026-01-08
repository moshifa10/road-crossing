import turtle as t
from player import Player
# I will be making the road crossing turtle game


# Set up the screen
screen = t.Screen()
screen.title("Road-Crossing Turtle")
screen.setup(width=600 , height=600)

screen.listen()
player = Player()

screen.onkey(fun=player.up, key="w")
screen.onkey(fun=player.go_right, key="d")
screen.onkey(fun=player.go_left, key="a")

game_is_on = True
while game_is_on:
    player.move()

screen.exitonclick()