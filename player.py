from turtle import Turtle
STARTING_POSITION = (0, -260)
MOVE_DISTANCE = 10
FINISH_LINE = 260


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.create_player()

    def create_player(self):
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.go_to_start()

    def go_forward(self):
        self.forward(MOVE_DISTANCE)

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE:
            return True
        else:
            return False
