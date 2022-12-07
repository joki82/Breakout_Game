from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("gray")
        self.resizemode("user")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.goto(0, -275)
        print(self.xcor(), self.ycor())
        self.speed(0)

    def small_paddle(self):
        """Paddle shrinks after the ball has broken through the red row and hit the upper wall"""
        self.shapesize(1, 3, 1)

    def move_left(self):
        if self.xcor() != -340:
            self.back(20)
            print(self.xcor(), self.ycor())

    def move_right(self):
        if self.xcor() != 340:
            self.forward(20)
            print(self.xcor(), self.ycor())

    def ball_speed(self):
        """Ball speed increases at specific intervals: after four hits, after twelve hits,
        and after making contact with the orange and red rows."""
        pass
