from turtle import Turtle
class paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        #self=Turtle()#write or not dont matter
        self.shape("square")
        self.penup()
        self.color("red")
        self.goto(position)#positio mean (x,y) single cordinate hi toh hoga
        self.shapesize(stretch_wid=5,stretch_len=1)#input is 20 timesgiven input hai,means in reality we want wid=100,len=20
    def goup(self):
        newy=self.ycor()+28
        self.goto(self.xcor(),newy)
    def godown(self):
        newy=self.ycor()-28
        self.goto(self.xcor(),newy)
   


    
    