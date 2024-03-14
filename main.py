from turtle import Screen
from board import Board, Scoreboard
from paddle import Paddle
from ball import Ball


scoreboard = Scoreboard()
paddle = Paddle((0, -375))
board = Board(scoreboard, paddle)
screen = Screen()
ball = Ball(paddle.position(), board)



screen.listen()
screen.onkey(paddle.go_right, "Right")
screen.onkey(paddle.go_left, "Left")

#Main Loop
game_is_on = True
while game_is_on:
    ball.move()
    screen.update()

    # Detect collision with the block
    for block in board.blocks:
        if ball.distance(block) < 25:  # Check the distance between ball and the block
            board.destroy_block(block)  # Remove the block from the board
            scoreboard.increment_score()  # Add the point
            ball.bounce_y()  # Bounce back

    # Detect collision with wall
    if ball.xcor() > 490 or ball.xcor() < -490:
        ball.bounce_x()

    # Detect collision with paddle
    elif ball.distance(paddle) < 30 and ball.ycor() > -360:
        ball.bounce_y()

    # Detect paddle misses
    elif ball.ycor() < -390:
        scoreboard.display_game_over()
        game_is_on = False

    # Detect collision with top of the board
    elif ball.ycor() > 390:
        ball.bounce_y()

    # Detect collision with the block
    for block in board.blocks:
        if ball .distance(block) < 25:  # Check the distance between ball and the block
            board.destroy_block(block)  # Remove the block from the board
            scoreboard.increment_score() # Add the point
            ball.bounce_y()  # Bounce back

    if board.check_win_condition():
        game_is_on = False


screen.mainloop()
