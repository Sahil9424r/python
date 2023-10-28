from turtle import Turtle,Screen
import random
#or

# import turtle as t
# timmy=t.Turtle()
timmy=Turtle()
# print(timmy)
myscreen=Screen()
timmy.shape("turtle")
timmy.color("blue")
#myscreen.exitonclick() #  come below jo kaam krna h each time

# CHALLENGE--

#TO MAKE SQUARE---

# timmy.forward(100)
# timmy.left(90)
# timmy.forward(100)
# timmy.left(90)
# timmy.forward(100)
# timmy.left(90)
# timmy.forward(100)
# timmy.left(90)

#or by loop--
# CHALLENGE--

#TO MAKE SQUARE---

#down..
# for i in range(4):
#     timmy.forward(100)
#     timmy.left(90)
# up..
# for i in range(4):
#     timmy.forward(100)
#     timmy.right(90)

# 
# for i in range(15):
#     timmy.penup()
#     timmy.forward(10) 

# for i in range(15):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()

#CHALLLENGE ---
#MAKE PENTAGON--

#upward
# for i in range(6):
#     timmy.forward(100)
#     timmy.left(72)
# myscreen.exitonclick() 
# #downward 
# for i in range(6):
#     timmy.forward(100)
#     timmy.right(72)
# myscreen.exitonclick() 

#TO MAKE BOTH TOGETHER-- JUST LOOP EK SAATH
# to make upwrard,....
# for i in range(4):
#     timmy.forward(100)
#     timmy.left(90)
# isa=True    
# while isa:
    
#         n=int(input("enter side length:"))
#         if n!=0:
#             for i in range(n):
#                 timmy.forward(100)
#                 timmy.left(360/n)
           
#         else:
#            isa=False
        #    myscreen.exitonclick() 


colors=["bisque","forest green","maroon","dark orange","dark orange","goldenrod"]
# to make downward,.....
# for i in range(4):
#     timmy.forward(100)
#     timmy.right(90)

# isa=True   
# while isa:
#   for n in range(3,19):
       
#         # n=int(input("enter side length:"))
#         if n!=0:
#             for i in range(n):
#                 timmy.forward(100)
#                 timmy.right(360/n)
#             timmy.color(random.choice(colors))  
#         else:
#            isa=False
#            myscreen.exitonclick() 

#BY ANGELA....

colors=["bisque","forest green","maroon","dark orange","dark orange","goldenrod"]
# def draw_shape(num_sides):
#     angle=360/num_sides
#     for _ in range(num_sides):
#         timmy.forward(100)
#         timmy.right(angle)
# for shape_sides in range(3,10):
#     timmy.color(random.choice(colors))
#     draw_shape(shape_sides)


myscreen.colormode(255)
direction=[0,90,180,270]
def randomc():#give mixture of colour
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    randomc=(r,g,b)
    return randomc


# # # timmy.pensize(50)
# timmy.speed("fastest")
# for _ in range(200):
#     timmy.color(random.choice(colors))
#     timmy.color(randomc())
#     timmy.forward(50)
#     # timmy.right(random.choice(direction))
#     # timmy.left(random.choice(direction))# or by dirct seatheading
#     timmy.setheading(random.choice(direction))
   
def spirograph(sizeofgap):
    for _ in range(int(360/sizeofgap)):
        timmy.color(randomc())
        timmy.circle(100)
      # heading gives starting and ending point
        timmy.setheading(timmy.heading()+sizeofgap)#if we remove +sizeofgap then not shift circ;e,just overlap
    # setheading is used to shift circle 
spirograph(10) #here number is for gap between circles
myscreen.exitonclick()     
# my_tuple=(1,3,8)
# print(my_tuple[0:2])
# # print(my_tuple[0])
# #tuple value cant be change
# #my_tuple[2]=12 not possible
# list(my_tuple)
# print(my_tuple)