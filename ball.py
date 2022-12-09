from turtle import Turtle


class Ball(Turtle):
    """Creates ball"""
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = -10
        self.y_move = -10
        self.move_speed = 0.1
        self.blocks_hit = 0
        self.first_org = 0
        self.first_red = 0

    def move(self):
        """Takes ball position adds 10/-10 and moves it to new position"""
        new_xcor = self.xcor() + self.x_move
        new_ycor = self.ycor() + self.y_move
        self.goto(new_xcor, new_ycor)

    def bounce_y(self):
        """When hits positive end of Y_cor, block or paddle, it changes y_move value from positive to
        negative and opposite"""
        self.y_move *= -1

    def bounce_x(self):
        """When hits sides of the screen, changes direction by changing x_move value from positive to
        negative and opposite"""
        self.x_move *= -1

    def restart(self):
        """Restart ball position to center of the screen, set speed to starting speed and reset blocks hit counter."""
        self.goto(0, 0)
        self.move_speed = 0.1
        self.blocks_hit = 0

    def ball_speed(self, hit, brick):
        """Ball speed increases at specific intervals: after four hits, after twelve hits,
        and after making contact with the orange and red rows."""
        self.blocks_hit += hit
        if self.blocks_hit == 4:
            self.move_speed *= 0.9
        elif self.blocks_hit == 12:
            self.move_speed *= 0.9
        elif brick.color() == ("orange", "orange") and self.first_org == 0:
            self.move_speed *= 0.9
            self.first_org += 1
        elif brick.color() == ("red", "red") and self.first_red == 0:
            self.move_speed *= 0.9
            self.first_red += 1
