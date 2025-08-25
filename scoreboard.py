from turtle import Turtle
class Scoreboard(Turtle):
    """
       A class to represent the scoreboard in the Pong game.

       Inherits from the `turtle.Turtle` class to display scores
       on the screen. Each scoreboard instance keeps track of
       an individual player's score.

       """

    def __init__(self,position):
        """
               Initialize the scoreboard at a specific position.

               Parameters
               ----------
               position : tuple
                   The (x, y) coordinates where the scoreboard will appear.
               """
        super().__init__()
        self.hideturtle()  # Hide the turtle pointer
        self.color("white")  # Set text color
        self.penup()
        self.goto(position)  # Position scoreboard
        self.score = 0  # Initial score
        self.update_score()  # Display initial score

    def update_score(self):
        """Clear the screen and update the score display."""
        self.clear()
        self.write(str(self.score), align="center", font=("Arial", 20, "bold"))
    def l_board_score(self):

        self.score = self.score + 1
        self.update_score()
    def r_board_score(self):
        self.score = self.score + 1
        self.update_score()