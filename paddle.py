from turtle import Turtle


class Paddle(Turtle):
    """Creates paddle and moving methods."""
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("gray")
        self.resizemode("user")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.goto(0, -275)
        self.speed(0)

    def small_paddle(self):
        """Paddle shrinks after the ball has broken through the red row and hit the upper wall"""
        self.shapesize(1, 3, 1)

    def move_left(self):
        """Moves paddle to left, limited to -340"""
        if self.xcor() != -340:
            self.back(20)


    def move_right(self):
        """Moves paddle to the right, limited to 340"""
        if self.xcor() != 340:
            self.forward(20)

    def reset_position(self):
        """Reset paddle position to starting position, after ball has been missed."""
        self.goto(0, -275)
