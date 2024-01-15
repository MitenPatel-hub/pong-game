# collision.py

class DetectCollision:
    """
    Class for detecting collisions in the Pong game.
    """
    def __init__(self):
        self.threshold = 30

    def is_collision_with_paddle(self, ball, paddle):
        """
        Checks if there is a collision between the ball and a paddle.

        The collision is detected based on the proximity of the ball to the paddle along both the x and y axes.
        A collision is considered to have occurred if:
        - The difference in y coordinates of the ball and paddle is less than 60 (close enough vertically).
        - The ball is located in front of the paddle (checked by comparing the absolute x coordinates).
        - The difference in x coordinates of the ball and paddle is less than the collision threshold.

        Args:
            ball (Ball): The ball object.
            paddle (Paddle): The paddle object.

        Returns:
            bool: True if there is a collision, False otherwise.
        """
        if (abs(ball.ycor() - paddle.ycor()) < 60) and (abs(ball.xcor()) < abs(paddle.xcor())):
            return abs(ball.xcor() - paddle.xcor()) < self.threshold
        return False

    @staticmethod
    def is_collision_with_wall(ball, vertical_wall):
        if ball.ycor() > vertical_wall - 40 or ball.ycor() < -vertical_wall + 40:
            return True
        return False

    @staticmethod
    def is_ball_past_paddle(ball, horizontal_wall):
        if ball.xcor() > horizontal_wall or ball.xcor() < -horizontal_wall:
            return True
        return False
