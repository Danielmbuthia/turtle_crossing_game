from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.finish_line_y = FINISH_LINE_Y
        self.shape('turtle')
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)
        self.level = 1

    def move_up(self):
        self.forward(MOVE_DISTANCE)

    def increase_level(self):
        self.level += 1

    def reset_player(self):
        self.goto(STARTING_POSITION)
