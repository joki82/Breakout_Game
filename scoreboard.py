from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()

        self.score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(260, 260)
        self.write(f"SCORE: {self.score}", align="center", font=("American Typewriter", 30, "normal"))

    def score_up(self, brick):
        if brick.color() == ("yellow", "yellow"):
            self.score += 1
            self.update_score()
        elif brick.color() == ("green", "green"):
            self.score += 3
            self.update_score()
        elif brick.color() == ("orange", "orange"):
            self.score += 5
            self.update_score()
        else:
            self.score += 7
            self.update_score()
