import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import ScoreBoard

screen = Screen()
screen.title("Turtle Crossing Game")
screen.screensize(600, 600)
screen.tracer(0)

player = Player()
scoreboard = ScoreBoard()
car = CarManager()

screen.listen()
screen.onkey(player.go_forward, "Up")

game_over = False
while not game_over:
    time.sleep(0.1)
    screen.update()
    car.create_cars()
    car.move_cars()

    # Detect collision with car
    for one_car in car.all_cars:
        if one_car.distance(player) < 25:
            game_over = True
            scoreboard.game_over()

    if player.is_at_finish_line():
        scoreboard.increase_level()
        player.go_to_start()
        car.level_up()


screen.exitonclick()
