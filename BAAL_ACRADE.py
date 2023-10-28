from turtle import Turtle
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.goto(0,0)
        self.x_move=10
        self.y_move=10
        self.movespeed=0.1

        # self.shapesize(stretch_wid=1,stretch_len=1)#as by defauly hots hia 
    def move(self):
        newx=self.xcor()+ self.x_move
        newy=self.ycor()+  self.y_move
        self.goto(newx,newy)
    def bouncey(self):#as upar se oppo mein neeche aaega
        self.y_move*=-1
       
    def bouncex(self):
        self.x_move*=-1
        self.movespeed*=0.9#aspaddle ke bhidne ke baad higa speed fast
    
    def resetposition(self):
        self.goto(0,0)
        self.movespeed=0.1
    
        self.bouncex()
