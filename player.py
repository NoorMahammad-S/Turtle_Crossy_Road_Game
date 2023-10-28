from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):

    def __init__(self):
        super().__init__()

        self.shape("turtle")
        self.penup()
        self.go_to_start()
        self.setheading(90)
        self.color("green")

    def player_move(self):
        self.forward(MOVE_DISTANCE)

    def player_back(self):
        self.back(MOVE_DISTANCE)

    def player_right(self):
        self.right(90)
        self.forward(MOVE_DISTANCE)
        self.left(90)

    def player_left(self):
        self.left(90)
        self.forward(MOVE_DISTANCE)
        self.right(90)

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def is_at_finish_ine(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False