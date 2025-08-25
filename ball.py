from turtle import Turtle
import time



class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.sleep_move = 0.1

    def ball_move(self):
        x_cor = self.xcor() +  self.x_move
        y_cor = self.ycor() + self.y_move #learn
        self.goto(x_cor, y_cor)



    def bounce_y(self):
       self.y_move *=-1 #learn

    def bounce_x(self):
        self.x_move *= -1
        self.sleep_move += 0.9