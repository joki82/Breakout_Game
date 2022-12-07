from turtle import Turtle


class Bricks(Turtle):
    def __init__(self):
        super().__init__()
        x_cor = -360
        y_cor = 250
        self.bricks_list = []
        for row in range(0, 8):
            for cell in range(0, 14):
                brick = Turtle("square")
                brick.penup()
                brick.resizemode("user")
                brick.shapesize(1, 2.5, 1)
                brick.goto(x_cor, y_cor)
                self.bricks_list.append(brick)
                x_cor += 55
                brick.color("red")
                if 1 < row < 4:
                    brick.color("orange")
                elif 3 < row < 6:
                    brick.color("green")
                elif 5 < row < 8:
                    brick.color("yellow")
            y_cor += -25
            x_cor = -360
