from turtle import Turtle

PACE = 20


class Player(Turtle):

    def __init__(self, starting_pos, controls):
        super().__init__()

        self.score = 0
        self.create_player(starting_pos)

        self.control_up = "w" if controls == "w" else "Up"
        self.control_down = "s" if controls == "w" else "Down"


    def create_player(self, starting_pos):

        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(starting_pos)

    def move_up(self):

        new_y = self.ycor()
        self.sety(PACE + new_y)

    def move_down(self):

        new_y = self.ycor()
        self.sety(-PACE + new_y)
