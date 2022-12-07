from turtle import Turtle, Screen
from paddle import Paddle
from bricks import Bricks
from ball import Ball
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Breakout Game")
screen.tracer(0)

paddle = Paddle()
bricks = Bricks()
ball = Ball()

screen.listen()
screen.onkey(paddle.move_left, "s")
screen.onkey(paddle.move_right, "d")

game_over = False

while not game_over:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    print(ball.xcor())
    # print(ball.ycor())
    # print(paddle.xcor(), paddle.ycor())
    # print(ball.distance(paddle))
    # print(ball.distance(bricks.bricks_list[0]))
    # print(paddle.distance(ball))

    if ball.ycor() > 290:
        ball.bounce_y()
    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.bounce_x()
    if ball.distance(paddle) < 50 and ball.ycor() < -260:
        ball.bounce_y()
screen.update()

screen.exitonclick()

if __name__ == '__main__':
    print('PyCharm')
