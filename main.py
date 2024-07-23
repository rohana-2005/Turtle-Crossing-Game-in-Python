import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from score import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.tracer(0)

player = Player()
screen.listen()
screen.onkey(player.up, "Up")

car_manager = CarManager()

score = Score()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.car_move()
    for i in car_manager.cars:
        if player.distance(i) < 27:
            score.over()
            game_is_on = False
    if player.ycor() > 290:
        player.reset()
        score.update_score()
        car_manager.speed_update()

screen.exitonclick()