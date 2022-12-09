from turtle import Turtle


class Scoreboard(Turtle):
    """Creates header containing current level(only first available at the moment), number of balls remaining and
    current score at right side."""
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()

        self.level = 1
        self.lives = 3
        self.score = 0
        self.update_display()
        self.level_end = False

    def update_display(self):
        """Updates screen after score or ball number changes."""
        self.clear()
        self.goto(-280, 260)
        self.write(f"Level: {self.level}", align="center", font=("American Typewriter", 30, "normal"))
        self.goto(0, 260)
        self.write(f"{self.lives}", align="center", font=("American Typewriter", 30, "normal"))
        self.goto(280, 260)
        self.write(f"Score: {self.score}", align="center", font=("American Typewriter", 30, "normal"))
        if self.lives == 0 or self.score == 448:
            self.goto(0, 20)
            self.write(f"Game over!", align="center", font=("American Typewriter", 30, "normal"))

    def score_up(self, brick):
        """Adds  points to score according brick value (yel=1, gre=3, org=5, red=7)."""
        if brick.color() == ("yellow", "yellow"):
            self.score += 1
            self.update_display()
        elif brick.color() == ("green", "green"):
            self.score += 3
            self.update_display()
        elif brick.color() == ("orange", "orange"):
            self.score += 5
            self.update_display()
        else:
            self.score += 7
            self.update_display()

    def lost_lives(self):
        """Deduct lives (ball), displays Game over."""
        self.lives -= 1
        if self.lives == 0:
            self.goto(0, 0)
            self.write(f"Game over", align="center", font=("American Typewriter", 30, "normal"))
        self.update_display()



