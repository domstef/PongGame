from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self, pos):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(pos)
        self.update()


    def update(self):
        self.write("{}".format(self.score), align="center", font=("Arial", 24, "normal"))

    def add_points(self):
        self.score += 1
        self.clear()
        self.update()

    def game_over_prompt(self):

        self.hideturtle()
        self.penup()
        self.goto(0, 0)
        self.write("Game over.", align="center", font=("Arial", 24, "normal"))