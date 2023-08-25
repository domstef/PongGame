from turtle import Turtle, Screen
from scoreboard import Scoreboard
from player import Player
from ball import Ball
import time

STARTING_POSITIONS_1 = (-350, 0)
STARTING_POSITIONS_2 = (350, 0)

SCREEN = Screen()
SCREEN.setup(800, 600)
SCREEN.bgcolor("black")
SCREEN.tracer(0)
SCREEN.listen()


class Pong:

    def __init__(self):
        self.game_on = True

        self.left_player = Player(STARTING_POSITIONS_1, "w")
        self.right_player = Player(STARTING_POSITIONS_2, "up")
        self.ball = Ball()

        self.left_score = Scoreboard((-200, 200))
        self.right_score = Scoreboard((200, 200))

        SCREEN.onkey(key=self.left_player.control_up, fun=self.left_player.move_up)
        SCREEN.onkey(key=self.left_player.control_down, fun=self.left_player.move_down)
        SCREEN.onkey(key=self.right_player.control_up, fun=self.right_player.move_up)
        SCREEN.onkey(key=self.right_player.control_down, fun=self.right_player.move_down)

        self.draw_line()
        SCREEN.update()

    def draw_line(self):

        line = Turtle()
        line.color("white")
        line.penup()
        line.goto(0, -300)
        line.pendown()
        for _ in range(33):
            line.setheading(90)
            line.forward(10)
            line.penup()
            line.forward(10)
            line.pendown()

    def game(self):

        while self.game_on:
            time.sleep(0.1)
            self.ball.move()
            self.ball.detect_collision_with_screen()

            right_requirement = self.ball.distance(self.right_player) < 50 and self.ball.xcor() > 320
            left_requirement = self.ball.distance(self.left_player) < 50 and self.ball.xcor() < -320

            if left_requirement or right_requirement:
                self.ball.bounce_x()

            if self.ball.xcor() == 400:
                self.left_score.add_points()
                self.ball.goto(0, 0)
            if self.ball.xcor() == -400:
                self.right_score.add_points()
                self.ball.goto(0, 0)

            SCREEN.update()

    def exit_player(self):
        SCREEN.exitonclick()
        self.game_on = False


game = Pong()
game.game()

game.exit_player()
