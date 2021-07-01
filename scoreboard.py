from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('black')
        self.penup()
        self.hideturtle()
        self.goto(-250, 250)
        self.level = 1
        self.write_level()

    def write_level(self):
        self.write("Level: {}".format(self.level), align="center", font=("Times New Roman", 20, "normal"))

    def add_level(self):
        self.level += 1
        self.clear()
        self.write_level()

    def game_over(self):
        self.clear()
        self.penup()
        self.hideturtle()
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Times New Roman", 50, "normal"))
        self.penup()
        self.hideturtle()
        self.goto(0, -20)
        self.write_level()
