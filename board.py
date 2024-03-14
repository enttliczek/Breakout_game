from turtle import Turtle, Screen
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]


class Board(Turtle):

    def __init__(self, scoreboard, paddle):
        self.screen = Screen()
        self.screen.bgcolor("black")
        self.screen.setup(width=1000, height=800)
        self.screen.title("Breakout")
        self.screen.tracer(0)
        self.screen.listen()
        self.scoreboard = scoreboard
        self.paddle = paddle
        self.blocks = []
        self.create_blocks()

    def create_blocks(self):
        block_height = 20
        block_width = 100
        gap = 5
        padding = 50
        for j in range(0, 4):  # for y axis
            row_color = random.choice(COLORS)
            for i in range(0, 10):  # for x axis
                new_block = Turtle("square")
                new_block.shapesize(stretch_wid=block_height/20, stretch_len=block_width/20)
                new_block.penup()
                new_block.color(row_color)
                new_block.goto(-self.screen.window_width() / 2 + padding + i * (block_width + gap),
                               j * (block_height + gap) + 100)
                self.blocks.append(new_block)
        self.screen.update()
        self.scoreboard.add_obstacle(new_block)

    def destroy_block(self, block):
        block.hideturtle()
        self.blocks.remove(block)
        self.scoreboard.increment_score()

    def blocks(self):
        return self.blocks


    def check_win_condition(self):
        if self.scoreboard.all_obstacles_destroyed():
            self.scoreboard.win()
            return True
        return False


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(0, 360)
        self.color("white")
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Arial", 16, "normal"))

    def display_game_over(self):
        self.goto(0, -50)
        self.write("Game Over", align="center", font=("Courier", 36, "normal"))

    def add_obstacle(self, obstacle):
        self.obstacle = obstacle

    def increment_score(self):
        self.score += 1
        self.update_scoreboard()
        self.screen.update()

    def all_obstacles_destroyed(self):
        return False
