from turtle import Turtle, Screen
from paddle import Paddle
from bricks import Bricks
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Breakout Game")
screen.tracer(0)

paddle = Paddle()
bricks = Bricks()
ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkey(paddle.move_left, "s")
screen.onkey(paddle.move_right, "d")

game_over = False


while not game_over:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    print(ball.xcor())
    print(ball.ycor())
    # print(paddle.xcor(), paddle.ycor())
    # print(ball.distance(paddle))
    # print(ball.distance(bricks.bricks_list[0]))
    # print(paddle.distance(ball))

    if ball.ycor() > 290:
        ball.bounce_y()
    if ball.xcor() > 375 or ball.xcor() < -375:
        ball.bounce_x()
    if ball.ycor() < -275:
        ball.restart()
        ball.move()
    if ball.distance(paddle) < 50 and ball.ycor() < -245:
        ball.bounce_y()
    for brick in bricks.bricks_list:
        if ball.distance(brick) < 33:
            brick.goto(1000, 1000)
            ball.bounce_y()
            score.score_up(brick)


screen.update()

screen.exitonclick()

if __name__ == '__main__':
    print('PyCharm')
