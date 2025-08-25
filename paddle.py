from turtle import Turtle

class Paddle(Turtle):
    """
        A Paddle object for the Pong game, inherited from the Turtle class.

        The paddle can move up and down along the screen.
        It is represented as a stretched square using Turtle graphics.
"""
    def __init__(self,position):
        """
            Initialize the paddle with a given position.

            Parameters
            ----------
            position : tuple
                The (x, y) coordinates for the paddle's initial location.
            """
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5 ,stretch_len=1, outline=1)
        self.penup()
        self.color("white")
        self.goto(position)


    def up(self):
        """Move the paddle upward by 20 units."""
        new_y_cor = self.ycor() + 20
        self.goto(self.xcor(), new_y_cor)

    def down(self):
        """Move the paddle downward by 20 units."""
        new_y_cor = self.ycor() - 20
        self.goto(self.xcor(), new_y_cor)
