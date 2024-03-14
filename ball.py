from turtle import Turtle


class Ball(Turtle):

    def __init__(self, paddle_position, board):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.goto(paddle_position[0], paddle_position[1] + 20)
        self.x_move = 3
        self.y_move = 3
        self.move_speed = 0.01
        self.board = board

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def reset_position(self, paddle_position):
        self.goto(paddle_position[0], paddle_position[1] + 20)
        self.move_speed = 0.01
        self.bounce_y()