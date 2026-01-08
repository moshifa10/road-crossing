import turtle as t
from player import Player
# I will be making the road crossing turtle game


# Set up the screen
screen = t.Screen()
screen.title("Road-Crossing Turtle")
screen.setup(width=600 , height=600)
screen.tracer(0)

screen.listen()
player = Player()

screen.onkey(fun=player.up, key="w")
screen.onkey(fun=player.go_right, key="d")
screen.onkey(fun=player.go_left, key="a")

 
 
game_is_on = True
while game_is_on:
    screen.update()
    # Detect player if is colliding with a wall and make the player not to move more than the wall
    if player.x_cor < -280 :
        player.x_cor += 20
    elif player.x_cor > 280:
        player.x_cor -= 20
    
    player.move()

screen.exitonclick()