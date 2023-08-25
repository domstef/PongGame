from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()

        self.pace_x = 10
        self.pace_y = 10
        self.score_1 = 0
        self.score_2 = 0

        self.ball_moving = True

    def move(self):
        nex_x = self.xcor() + self.pace_x
        new_y = self.ycor() + self.pace_y
        self.goto(nex_x, new_y)

    def detect_collision_with_screen(self):
        if self.ycor() > 280 or self.ycor() < -280:
            print("Collision!")
            self.bounce_y()


    def bounce_y(self):
        self.pace_y *= -1

    def bounce_x(self):
        self.pace_x *= -1


