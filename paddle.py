from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=8)
        self.penup()
        self.goto(position)
        self.screen = self.getscreen()
        self.screen.update()

    def go_left(self):
        new_x = self.xcor() - 40
        if new_x > -self.screen.window_width()/2:  # Check if the new x-coordinate is within the screen bounds
            self.goto(new_x, self.ycor())
            self.screen.update()

    def go_right(self):
        new_x = self.xcor() + 40
        if new_x < self.screen.window_width()/2:  # Check if the new x-coordinate is within the screen bounds
            self.goto(new_x, self.ycor())
            self.screen.update()
