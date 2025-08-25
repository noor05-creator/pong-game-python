from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self,position):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(position)
        self.score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(str(self.score), align="center", font=("Arial", 20, "bold"))
    def l_board_score(self):
        self.score = self.score + 1
        self.update_score()
    def r_board_score(self):
        self.score = self.score + 1
        self.update_score()