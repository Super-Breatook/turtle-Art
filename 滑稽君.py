﻿import turtle
import time
start = time.perf_counter()
turtle.speed(100)
turtle.hideturtle()
 
#画整体部分
turtle.penup()
turtle.pensize(5)
turtle.goto(-10,-200)
turtle.pendown()
turtle.color("yellow")
turtle.begin_fill()
turtle.fillcolor("yellow")
turtle.circle(200)
turtle.end_fill()
turtle.penup()
 
 
#画左眼
turtle.color("orange")
turtle.pensize(1)
turtle.goto(-110,80)
turtle.pendown()
turtle.begin_fill()
turtle.fillcolor("white")
turtle.seth(150)
turtle.pendown()
turtle.circle(145,64)
turtle.penup()
turtle.goto(-110,80)
turtle.pendown()
turtle.seth(-30)
turtle.circle(-25,150)
turtle.seth(155)
turtle.circle(140,55)
turtle.seth(150)
turtle.seth(180)
turtle.circle(-26,172)
turtle.end_fill()
turtle.color("black")
turtle.begin_fill()
turtle.fillcolor("black")
turtle.circle(-25)
turtle.end_fill()
turtle.penup()
 
#画右眼
turtle.color("orange")
turtle.goto(190,80)
turtle.pensize(1)
turtle.goto(190,80)
turtle.pendown()
turtle.begin_fill()
turtle.fillcolor("white")
turtle.seth(150)
turtle.pendown()
turtle.circle(145,64)
turtle.penup()
turtle.goto(190,80)
turtle.pendown()
turtle.seth(-30)
turtle.circle(-25,150)
turtle.seth(155)
turtle.circle(140,55)
turtle.seth(150)
turtle.seth(180)
turtle.circle(-26,172)
turtle.end_fill()
turtle.color("black")
turtle.begin_fill()
turtle.fillcolor("black")
turtle.circle(-25)
turtle.end_fill()
turtle.penup()
 
 
#画左眉
turtle.color("black")
turtle.seth(0)
turtle.goto(-180,150)
turtle.pendown()
turtle.pensize("25")
turtle.circle(-100,60)
turtle.penup()
 
#画右眉
turtle.seth(180)
turtle.goto(120,150)
turtle.pendown()
turtle.pensize("25")
turtle.circle(100,60)
turtle.penup()
 
 
#画嘴
turtle.goto(-130,-50)
turtle.seth(262)
for i in range(90):
    turtle.pensize(i*0.25)
    turtle.pendown()
    turtle.color("brown")
    turtle.circle(120,1.1)
for i in range(85):
    turtle.pensize(22.5 - 0.25*i)
    turtle.pendown()
    turtle.circle(120, 1.1)
turtle.penup()

#左腮红
turtle.color("red")
turtle.goto(-100,-5)
turtle.pensize(1)
turtle.seth(0)
turtle.pendown()
turtle.seth(90)
turtle.begin_fill()
turtle.fillcolor("red")
for i in range(2):
    for j in range(10):
        turtle.fd(j)
        turtle.left(9)
    for j in range(10,0,-1):
        turtle.fd(j)
        turtle.left(9)
turtle.end_fill()
turtle.penup()
 
 
#右腮红
turtle.color("red")
turtle.goto(160,-5)
turtle.pensize(1)
turtle.seth(0)
turtle.pendown()
turtle.seth(90)
turtle.begin_fill()
turtle.fillcolor("red")
for i in range(2):
    for j in range(10):
        turtle.fd(j)
        turtle.left(9)
    for j in range(10,0,-1):
        turtle.fd(j)
        turtle.left(9)
turtle.end_fill()

print('已完成')
turtle.done()
