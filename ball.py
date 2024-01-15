# ball.py
from turtle import Turtle
from utils import get_user_input


class Ball(Turtle):
    """
    Class representing the ball in the Pong game.

    Attributes:
        dx (int): The ball's movement along the x-axis.
        dy (int): The ball's movement along the y-axis.
    """
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.get_ball_settings()
        self.penup()
        self.dx = 10
        self.dy = 10
        self.move_speed = 0.1

    def get_ball_settings(self):
        """
        Retrieves user input for customizing the ball settings.
        """
        self.shape(get_user_input("Shape of the ball", "circle", str))
        self.color(get_user_input("Color of the ball", "white", str))

    def move(self):
        """
        Moves the ball in the current direction.
        """
        new_x = self.xcor() + self.dx
        new_y = self.ycor() + self.dy
        self.goto(new_x, new_y)

    def bounce_y(self):
        """
        Reverses the ball's y-axis movement direction.
        """
        self.dy *= -1

    def bounce_x(self):
        """
        Reverses the ball's x-axis movement direction.
        """
        self.dx *= -1

    def reset_position(self):
        """
        Resets the ball to the center and reverses its direction.
        """
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()
