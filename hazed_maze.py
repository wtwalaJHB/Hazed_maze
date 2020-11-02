"""
[Module] In maze package
"""
import random
import turtle 
from turtle import Turtle, Screen



window = turtle.Screen()
pointer = turtle.Turtle()

obstacles_list = []
row_list = []
col_list = []
grid  = []

# area limit vars
min_y, max_y = -200, 200
min_x, max_x = -100, 100


def create_obstacles():
    """
    creates the obstacles
    """
    
    global obstacles_list,grid
    
    for x in range(-200,200,20):
        count = 0
        for i in range(20):
            row_list.append((-100+count,x))
            count += 10
    
    for x in range(-100,100,40):
        count = 0
        for i in range(40):
            col_list.append((x,-200+count))
            count += 10
    
    obstacles_list=[(x,y) for (x,y) in col_list
                    if (x,y) not in obstacles_list]
    for x,y in row_list:
        obstacles_list.append((x,y))

    
    for i in range(random.randrange(200,250)):
        random.choices(obstacles_list.pop(random.randrange(
            len(obstacles_list)-1)))   

    for i in obstacles_list:
        if i == (-10,0) or i == (-10,10) or i == (10,10) or i == (0,0):
            obstacles_list.remove(i)
        else:
            grid.append(i)
            
            
def draw_obstacles():
    """
    draws the obstacles on to the window
    """
    
    pointer.penup()
    pointer.goto(-100,-200)
    pointer.pen(pencolor='black')  
    turtle.tracer(False)
    for i in obstacles_list:
        pointer.goto(i)
        pointer.pendown()
        pointer.fillcolor('light blue')
        pointer.begin_fill()
        for i in range(4):
            pointer.fd(10)
            pointer.lt(90)
        pointer.end_fill()
        pointer.penup()
    turtle.tracer(True)
    pointer.color('red','red')
    
     
def draw_world():
    """
    create world:
        create the world constraints
    """

    pointer.pen(pencolor='red',pensize='2')
    pointer.speed(-1)
    pointer.penup()
    pointer.goto(max_x,0)
    pointer.pendown()
    pointer.goto(max_x,0)
    pointer.goto(max_x,min_y)    
    pointer.goto(min_x,min_y)        
    pointer.goto(min_x,max_y)
    pointer.goto(max_x,max_y)
    pointer.goto(max_x,0)
    pointer.penup()
    pointer.home()
    pointer.left(90)
    pointer.hideturtle()   


create_obstacles()
draw_obstacles()
draw_world()
pointer.home()
pointer.lt(90)
pointer.showturtle()
    
turtle.mainloop()


