from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.refresh_score()
        self.color("white")
        self.penup()
        self.goto(0, 280)
        self.hideturtle()
        self.refresh_score()


    def refresh_score(self):
        self.write(f"Score: {self.score}", False, "center", ("Arial", 14, "normal"))

    def increase_score(self):
        self.score +=1
        self.clear()
        self.refresh_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER. Score: {self.score}", False, "center", ("Arial", 14, "normal"))