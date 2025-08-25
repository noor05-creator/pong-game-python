from turtle import Turtle
import time



class Ball(Turtle):
    """
      A Ball class that inherits from the Turtle class.
      Represents the ball used in a Pong-like game.

      Attributes
      ----------
      x_move : int
          The step size of the ball along the X-axis.
      y_move : int
          The step size of the ball along the Y-axis.
      sleep_move : float
          The ball's movement speed (used to control the delay between frames).
      """
    def __init__(self):
        """
                Initializes the Ball object with default shape, size, color, and movement values.
                """
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.color("white")
        self.penup()
        self.x_move = 10  # Initial horizontal movement step
        self.y_move = 10  # Initial vertical movement step
        self.sleep_move = 0.1  # Delay time (controls speed)

    def ball_move(self):
        """
              Moves the ball by updating its X and Y coordinates
              based on the current movement steps.
              """
        x_cor = self.xcor() +  self.x_move
        y_cor = self.ycor() + self.y_move #learn
        self.goto(x_cor, y_cor)



    def bounce_y(self):
        """
        Reverses the ball's vertical direction when it collides
        with the top or bottom wall.
        """

        self.y_move *=-1 #learn

    def bounce_x(self):
        """
        Reverses the ball's horizontal direction when it collides
        with a paddle. Also increases the speed slightly.
        """
        self.x_move *= -1
        self.sleep_move += 0.9