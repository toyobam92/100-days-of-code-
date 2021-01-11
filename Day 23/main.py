import time
from turtle import Turtle, Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
car_manager = CarManager()
score_board = Scoreboard()

game_on = True
screen.listen()
screen.onkey(player.go_up, "Up")

while game_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    # Detect collision
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_on = False
            score_board.game_over()

    # Detect a successful crossing
    if player.finish_line():
        player.go_to_start()
        car_manager.level_up()
        score_board.level_update()

screen.exitonclick()
