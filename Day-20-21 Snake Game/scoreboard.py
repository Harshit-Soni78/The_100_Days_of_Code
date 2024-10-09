from turtle import Turtle
ALIGNMENT = 'center'
FONT = ("Courier",16,"bold")
class Score:
    def __init__(self):
        self.score = 0
        self.scoreboard = Turtle()
        self.scoreboard.hideturtle()
        self.scoreboard.setposition(x=0, y=270)
        self.scoreboard.color("white")
        self.scoreboard.write(arg="Score: " + str(self.score), align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.scoreboard.clear()
        self.score += 1
        self.scoreboard.write(arg="Score: " + str(self.score), align=ALIGNMENT, font=FONT)


    def game_over(self):
        self.scoreboard.goto(0,0)
        self.scoreboard.write("GAME OVER ", align= ALIGNMENT , font= FONT)