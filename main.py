import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# player
player = Player()
# car
car_manager = CarManager()
# scoreboard
scoreboard = Scoreboard()

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

screen.listen()
screen.onkey(fun=player.move_up, key="Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # cars
    car_manager.create_car()
    car_manager.move_cars()

    # detect if player reach the top
    if player.is_at_finish_line():
        scoreboard.increase_level()
        player.reset_player()
        car_manager.increase_speed()

    # detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()
