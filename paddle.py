# paddle.py
from turtle import Turtle
from utils import get_user_input


class Paddle(Turtle):
    """
    Class representing a paddle in the Pong game.

    Attributes:
        position (tuple): The starting position of the paddle.
    """
    def __init__(self, position, vertical_wall_height):
        super().__init__()
        self.wall_height = vertical_wall_height
        self.shape("square")
        self.color("white")
        self.get_paddle_color()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def get_paddle_color(self):
        """
        Retrieves user input for customizing the paddle color.
        """
        self.color(get_user_input("Color of the paddle", "white", str))

    def go_up(self):
        """
        Moves the paddle up by a fixed amount.
        """
        new_y = self.ycor() + 20
        if new_y + 60 <= self.wall_height:
            self.goto(self.xcor(), new_y)

    def go_down(self):
        """
        Moves the paddle down by a fixed amount.
        """
        new_y = self.ycor() - 20
        if new_y - 60 >= -self.wall_height:
            self.goto(self.xcor(), new_y)
