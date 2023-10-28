from turtle import Turtle
class scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.lscore=0
        self.rscore=0
        self.updatescore()
    def updatescore(self):
        self.clear()
        self.goto(-100,200)
        self.write(self.lscore,align="center",font=("Courier",80,"normal"))
        self.goto(100,200)
        self.write(self.rscore,align="center",font=("Courier",80,"normal"))#write ,ext at current turtle pos
    def lpoint(self):
        self.lscore+=1
        self.updatescore()
    def rpoint(self):
        self.rscore+=1
        self.updatescore()