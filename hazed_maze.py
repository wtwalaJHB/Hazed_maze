"""
[Module] In maze package
"""
import random
from turtle import Turtle, Screen


obstacles_list = []
pointer = Turtle()


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
            obstacles_list.append((-90+count,x))
            count += 10
    
    for x in range(-100,100,40):
        count = 0
        for i in range(40):
            obstacles_list.append((x,-200+count))
            count += 10
   
    for i in range(random.randrange(180,230)):
        random.choices(obstacles_list.pop(random.randrange(
            len(obstacles_list)-1)))   

    for i in obstacles_list:
        if i == (-10,0) or i == (-10,10) or i == (10,10) or i == (0,0) or i == (-10,-20) or i == (10,20) or i[0] >= 100:   
            obstacles_list.remove(i)
        elif i[0] in range (-30, 31) and i[1] in range (-30, 31):
            obstacles_list.pop(obstacles_list.index(i))
        elif i[0] in range(-11,11) and i[1] in range(-11,11):
            obstacles_list.remove(i)
       
    return obstacles_list
            
            
def draw_obstacles():
    """
    draws the obstacles on to the window
    """
    window,turtle = main()
    pointer.penup()
    pointer.goto(obstacles_list[0])
    pointer.pen(pencolor= 'blue')  
    pointer.speed(0)
    window.tracer(False)
    for i in obstacles_list:
        pointer.goto(i)
        pointer.pendown()
        pointer.fillcolor('teal')
        pointer.begin_fill()
        for i in range(4):
            pointer.fd(10)
            pointer.lt(90)
        pointer.end_fill()
        pointer.penup()
    window.tracer(True)

    pointer.color('red','red')
    pointer.pendown()
  
     
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
    pointer.pendown()
    # pointer.hideturtle()


def is_position_blocked(x, y):
    """
    is position blocked
        checkes if the co-ordinates have an obstacle
        return a bool
    """
    global obstacles_list


    for x1,y1 in obstacles_list:
        if (x in range(x1,x1+10)) and (y in range(y1,y1+10)):
            return True
    return False
  

def is_path_blocked(x1, y1, x2, y2):
    """
    is path blocked
        checks if the position it has to move to is blocked
        returns a bool 
    """
    global obstacles_list

    if x1 == x2:       
        for x,y in obstacles_list:
            for a in range(y1,y2):
                if x1 in range(x,x+10) and a in range(y,y+10):
                    return True
    elif y1 == y2: 
        for x,y in obstacles_list:
            for a in range(x1,x2):
                if a in range(x,x+10) and y1 in range(y,y+10):
                    return True



    return False


def get_obstacles():
    
    return obstacles_list


def main():
    window = Screen()
    window_turtles = window.turtles()
    [window_turtles.remove(i) for i in window_turtles]
    pointer.hideturtle()
    return window,pointer
    
    