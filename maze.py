import turtle
import _thread
import time

class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y

class Line:
    def __init__(self,p1,p2):
        self.p1=p1
        self.p2=p2

paths = set()
turtle.tracer(0,0)

# http://bryceboe.com/2006/10/23/line-segment-intersection-algorithm/
def ccw(A,B,C):
    return (C.y-A.y) * (B.x-A.x) > (B.y-A.y) * (C.x-A.x)
def intersect(A,B,C,D):
    return ccw(A,C,D) != ccw(B,C,D) and ccw(A,B,C) != ccw(A,B,D)

# barrier on circle
def circle(r, a):
    a / 22.5
    for _ in enumerate(range(int(a / 22.5))):
        p1 = Point(turtle.pos()[0], turtle.pos()[1])
        turtle.circle(r,22.5)
        p2 = Point(turtle.pos()[0], turtle.pos()[1])
        paths.add(Line(p1,p2))

# barrier on line
def line():
    turtle.right(90)
    turtle.pendown()
    turtle.forward(20)
    p1 = Point(turtle.pos()[0], turtle.pos()[1])
    turtle.backward(20)
    p2 = Point(turtle.pos()[0], turtle.pos()[1])
    turtle.left(90)
    paths.add(Line(p1,p2))

# sample maze
def sampleMaze1():
    turtle.penup()

    # inner circle
    turtle.right(-90)
    turtle.forward(40)
    turtle.left(90)
    line()
    turtle.pendown()
    #turtle.circle(40,135)
    circle(40,135)
    line()
    turtle.penup()
    circle(40,45)
    line()
    circle(40,90)
    line()
    circle(40,45)
    line()
    circle(40,45)
    turtle.penup()
    turtle.home()

    # 1st
    turtle.right(-90)
    turtle.forward(60)
    turtle.left(90)
    turtle.pendown()
    circle(60, 22.5)
    line()
    circle(60, 90-22.5)
    turtle.penup()
    circle(60, 22.5)
    turtle.pendown()
    circle(60, 45)
    line()
    turtle.penup()
    circle(60, 22.5) # 180
    line()
    turtle.penup()
    circle(60, 22.5)
    turtle.pendown()
    circle(60, 45)
    line()
    turtle.penup()
    circle(60, 22.5)
    line()
    turtle.pendown()
    circle(60, 22.5)
    turtle.penup()
    circle(60, 45)
    line()
    turtle.penup()
    circle(60, 22.5)
    turtle.home()

    # 2nd
    turtle.right(-90)
    turtle.forward(80)
    turtle.left(90)
    line()
    turtle.penup()
    circle(80, 45)
    turtle.pendown()
    circle(80, 45+90-22.5)
    turtle.penup()
    circle(80, 22.5)
    line()
    turtle.pendown()
    circle(80, 45)
    turtle.penup()
    circle(80,22.5)
    line()
    turtle.penup()
    circle(80,45)
    line()
    turtle.penup()
    circle(80,22.5)

    turtle.pendown()
    circle(80, 45)
    turtle.penup()
    turtle.home()

    # 3rd
    turtle.right(-90)
    turtle.forward(100)
    turtle.left(90)
    turtle.pendown()
    circle(100, 360-22.5)
    turtle.penup()
    turtle.home()

def isBlocked(agent_path):
    for path in paths:
        print(intersect(agent_path.p1,agent_path.p2, path.p1,path.p2))

sampleMaze1()
turtle.tracer(1,1)
paths = list(paths)
agent_path = Line(paths[1].p1,paths[1].p2)
isBlocked(paths[0])
turtle.mainloop()