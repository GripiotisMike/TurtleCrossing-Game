from turtle import Screen
from scoreboard import ScoreBoard
from cars import Car
from player import Player
import time

screen = Screen()
screen.title("Crossing Game")
screen.setup(600, 600)
screen.tracer(0)

scoreboard = ScoreBoard()
player = Player()
car_manager = Car()

screen.listen()
screen.onkey(player.move_up, "w")

counter = 1
game_on = True
while game_on:
    screen.update()
    time.sleep(0.05)
    car_manager.create_car()
    car_manager.move_car()
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_on = False
            scoreboard.game_over()
    if player.ycor() > 280:
        player.reset_player()
        car_manager.move_increase()
        scoreboard.next_lvl()
        counter += 1
    if counter == 10:
        game_on = False
        scoreboard.victory()

screen.exitonclick()
