# game_config.py
from turtle import Screen
from utils import get_user_input


class GameConfig:
    """
    Class to handle the configuration of the game, including the screen setup and user-customizable settings.

    Attributes:
        bg_color (str): Background color of the game screen.
        title (str): Title of the game.
        screen_width (int): Width of the game screen.
        screen_height (int): Height of the game screen.
        score_text_color (str): Color of the scoreboard text.
        screen (Screen): Turtle screen object for the game.
    """

    def __init__(self):
        self.bg_color = "black"
        self.title = "Pong Game"
        self.screen_width = 800
        self.screen_height = 600
        self.score_text_color = "white"
        self.screen = Screen()
        self.get_screen_settings()
        self.initialize_screen()

    def get_screen_settings(self):
        """
        Retrieves user input for customizing the game settings.
        """
        self.bg_color = get_user_input("Enter the background color for the game", self.bg_color, str)
        self.title = get_user_input("Enter the title of the game", self.title, str)
        self.screen_width = get_user_input("Enter the width of the screen", self.screen_width, int)
        self.screen_height = get_user_input("Enter the height of the screen", self.screen_height, int)
        self.score_text_color = get_user_input("Enter the scoreboard text color", self.score_text_color, str)
        self.validate_color_contrast()

    def validate_color_contrast(self):
        """
        Validates the contrast between the background color and the scoreboard text color.
        Prompts the user to choose a different text color if they are the same.
        """
        while self.bg_color.lower() == self.score_text_color.lower():
            print("The background color and text color are the same. Please choose a different text color.")
            self.score_text_color = get_user_input("Enter a different color for the scoreboard text", "white", str)

    def initialize_screen(self):
        """
        Initializes the game screen with the configured settings.
        """
        self.screen.bgcolor(self.bg_color)
        self.screen.title(self.title)
        self.screen.setup(width=self.screen_width, height=self.screen_height)
        self.screen.tracer(0)