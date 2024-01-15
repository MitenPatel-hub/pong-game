# main.py
import logging
from paddle import Paddle
from ball import Ball
from collision import DetectCollision
from score import Scoreboard
from game_config import GameConfig
import time
import turtle

# Configure logging to record events and errors to a log file.
logging.basicConfig(filename='pong_game.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


def end_game(x, y):
    """
    Ends the game, hides game objects, displays the game over message, and logs the final score.
    Schedules the game window to close after a delay to allow the game over message to be read.

    Parameters:
        x (int): The x-coordinate of the click. Not used in this function.
        y (int): The y-coordinate of the click. Not used in this function.
        Function signature matching: x and y parameters needed to allow response to a screen click event as an option for ending game.
    """
    global game_is_on
    # Hide the ball and paddles immediately
    ball.hideturtle()
    r_paddle.hideturtle()
    l_paddle.hideturtle()

    # Force the screen to update to reflect the changes
    screen.update()

    # Display the game over message on the screen
    score.game_over()

    # Set the game's running state to False to stop the game loop
    game_is_on = False

    # Log the final score to the game log
    logging.info(f"Game ended. Final score - Left: {score.l_score}, Right: {score.r_score}")

    # Use ontimer to call screen.bye after 2 seconds to ensure game over message is visible to user before window closes
    turtle.ontimer(screen.bye, 10000)  # 10000 milliseconds or 10 seconds delay


# Initialize game configuration settings
logging.info("Initializing game configuration")
game_config = GameConfig()

# Create the main game screen object from the game configuration
screen = game_config.screen


# Function to close the game screen, to be called after a delay
def close_screen():
    """
    Closes the Turtle graphics window.
    """
    screen.bye()


# Create the paddles, ball, collision detection, and scoreboard with user customization
logging.info("Creating game objects")
vertical_wall = game_config.screen_height // 2
horizontal_wall = game_config.screen_width // 2
r_paddle = Paddle((horizontal_wall - 50, 0), vertical_wall)
l_paddle = Paddle((-horizontal_wall + 50, 0), vertical_wall)
ball = Ball()
detect_collision = DetectCollision()
score = Scoreboard(vertical_wall - 100, game_config.score_text_color)
winning_score = 7  # The score required to win the game

# Set up the keyboard bindings for controlling the paddle movements
logging.info("Setting up keyboard bindings")
screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

# Bind the click event to the function that ends the game
screen.onclick(end_game)

# The main game loop
game_is_on = True
logging.info("Starting game loop")
while game_is_on:
    try:
        # Move the ball and update the screen
        time.sleep(ball.move_speed)
        screen.update()
        ball.move()

        # Handle collisions with paddles
        if detect_collision.is_collision_with_paddle(ball, r_paddle) or detect_collision.is_collision_with_paddle(ball, l_paddle):
            ball.bounce_x()
            ball.move_speed *= 0.9

        # Handle collisions with walls
        if detect_collision.is_collision_with_wall(ball, vertical_wall):
            ball.bounce_y()

        # Reset the ball position if it goes out of bounds and update the score
        if detect_collision.is_ball_past_paddle(ball, horizontal_wall):
            score.update_score(ball)
            ball.reset_position()

        # End the game if a player reaches the winning score
        if score.r_score == winning_score or score.l_score == winning_score:
            end_game(0, 0)

    # Exception handling for any unexpected errors during game execution
    except turtle.TurtleGraphicsError as tge:
        logging.exception("A Turtle graphics error occurred: %s", tge)
        break
    except ValueError as ve:
        logging.exception("A value error occurred in game logic: %s", ve)
        break
    except Exception as e:
        logging.exception("An unexpected error occurred: %s", e)
        break

# Log that the game loop has ended
logging.info("Game loop ended")

# Ensure the screen stays open until after the timer expires
turtle.done()
