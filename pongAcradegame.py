from turtle import Turtle ,Screen
from paddle import paddle
from BAAL_ACRADE import Ball
from ArcadeScore import scoreboard
import time
screen=Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("PONG") 
# turtle=Turtle()
# turtle.shape("square")
screen.tracer(0)#stop animation,then by update function it works ,but by loop
# turtle.penup()
lpad=paddle((350,0))
rpad=paddle((-350,0))
screen.listen()
screen.onkey(rpad.goup,"Up")
screen.onkey(rpad.godown,"Down")
screen.onkey(lpad.goup,"w")
screen.onkey(lpad.godown,"s")
#my paddle is not moving,our code is right but there is problem in turtle module,said by angela yu ,as uska bhi not properly move,as only singlemove or button not work
ball=Ball()
ball.penup()
score=scoreboard()

# ball=Turtle()
# ball.shape("circle")
# ball.color("white")#or by class
# ball.goto(0,0)
# ball.shapesize(stretch_wid=1,stretch_len=1)#input is 20 timesgiven input hai,means in reality we want wid=100,len=20
# turtle.color("red")
# turtle.goto(350,0)
# turtle.shapesize(stretch_wid=5,stretch_len=1)#input is 20 timesgiven input hai,means in reality we want wid=100,len=20
# screen.listen()
# def go():
#     newy=turtle.ycor()+28
#     turtle.goto(turtle.xcor(),newy)
# def down():
#     newy=turtle.ycor()-28
#     turtle.goto(turtle.xcor(),newy)
# def left():
#     newx=turtle.xcor()-28
#     turtle.goto(newx,turtle.ycor())    
# def right():
#     newx=turtle.xcor()+28
#     turtle.goto(newx,turtle.ycor())

        
game=True
while game:
    time.sleep(ball.movespeed)
    screen.update()
   
    ball.move()
    if ball.ycor()>290 or ball.ycor()<-290:
        ball.bouncey() 
    if (ball.distance(rpad)<50 and ball.xcor()>320 ) or (ball.distance(lpad)<50 and ball.xcor()<-320 ) :
        ball.bouncex()  
       
    if ball.xcor()>380:
        ball.resetposition()
        score.lpoint()

    if ball.xcor()<-380:
        ball.resetposition()  
        score.rpoint()     
screen.exitonclick() 