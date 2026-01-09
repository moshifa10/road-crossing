import turtle as t
from player import Player
from cars import Cars
import time
# I will be making the road crossing turtle game


# Set up the screen
screen = t.Screen()
screen.title("Road-Crossing Turtle")
screen.setup(width=600 , height=600)
screen.colormode(255)
screen.tracer(0)

screen.listen()
player = Player()

screen.onkey(fun=player.up, key="w")
screen.onkey(fun=player.go_right, key="d")
screen.onkey(fun=player.go_left, key="a")

cars = Cars(300)

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    # Detect player if is colliding with a wall and make the player not to move more than the wall
    if player.x_cor < -280 :
        player.x_cor += 20
    elif player.x_cor > 280:
        player.x_cor -= 20
    

    player.move()

    # Make cars be visible 
    for each_car in cars.all_cars:
        cars.move(each_car)
        
        # Check if player collided with the car
        if player.distance(each_car) < 15:
            game_is_on = False

screen.exitonclick()