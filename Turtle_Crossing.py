from turtle import Screen
from scoreboard import ScoreBoard
from cars import Car
from player import Player
import time

# Set up the screen
screen = Screen()
screen.title("Crossing Game")  # Set the title of the window
screen.setup(600, 600)  # Set the window size
screen.tracer(0)  # Disable automatic screen updates for smoother gameplay

# Initialize game components
scoreboard = ScoreBoard()
player = Player()
car_manager = Car()

# Listen for key presses to move the player
screen.listen()
screen.onkey(player.move_up, "w")  # 'w' key to move up

counter = 1  # Counter to track levels
game_on = True  # Flag to control the game loop
while game_on:
    screen.update()  # Update the screen after each iteration
    time.sleep(0.05)  # Delay to control game speed

    # Create and move cars
    car_manager.create_car()
    car_manager.move_car()

    # Check for collision between player and any car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:  # If player collides with car
            game_on = False  # End the game
            scoreboard.game_over()  # Display game over message

    # Check if player reaches the top of the screen to level up
    if player.ycor() > 280:  # Player reaches top
        player.reset_player()  # Reset player to starting position
        car_manager.move_increase()  # Increase car speed
        scoreboard.next_lvl()  # Move to the next level
        counter += 1  # Increase level counter

    # End game if player reaches level 10
    if counter == 10:
        game_on = False
        scoreboard.victory()  # Display victory message

screen.exitonclick()  # Wait for a click to close the window
