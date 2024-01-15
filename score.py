# score.py
from turtle import Turtle


class Scoreboard(Turtle):
    """
    Class for managing the game's scoreboard.

    Attributes:
        top_wall_y_value (int): Y-coordinate of the top wall for positioning the scoreboard.
        r_score (int): Score of the right player.
        l_score (int): Score of the left player.

    Methods:
        update_scoreboard(): Updates the display of scores.
        game_over(): Displays the game over message.
    """
    def __init__(self, top_wall_y_value, score_text_color="white"):
        super().__init__()
        self.top_wall_y_value = top_wall_y_value
        self.score_text_color = score_text_color
        self.r_score = 0
        self.l_score = 0
        self.setup_scoreboard()

    def setup_scoreboard(self):
        """
        Sets up the initial appearance of the scoreboard.
        """
        self.color(self.score_text_color)
        self.penup()
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        """
        Clears the current scores and writes the new scores on the screen.
        """
        self.clear()
        self.goto(-100, self.top_wall_y_value)
        self.write(self.l_score, align="center", font=("Courier", 80, "bold"))
        self.goto(100, self.top_wall_y_value)
        self.write(self.r_score, align="center", font=("Courier", 80, "bold"))

    def update_score(self, ball):
        """
        Updates the score based on the ball's position. Increments the score for the left or right player
        depending on which side the ball goes out of bounds.

        Args:
            ball (Ball): The ball object to check its x-coordinate.
        """
        if ball.xcor() > 0:
            self.l_score += 1
        else:
            self.r_score += 1
        self.update_scoreboard()

    def game_over(self):
        """
        Displays the 'GAME OVER' message.
        """
        self.clear()
        self.goto(0, 0)
        self.write(f"Final score - Left: {self.l_score}, Right: {self.r_score}", align="center", font=("Courier", 28, "bold"))
