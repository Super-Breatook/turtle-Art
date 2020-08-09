import turtle


turtle.speed(100)
turtle.hideturtle()
turtle.color('red')

turtle.tracer(238)
for x in range(39):
    turtle.forward(100)
    
    for y in range(237):
        turtle.left(1)
        turtle.forward(1)
        
    turtle.forward(100)
turtle.tracer(True)

print("已完成")
turtle.done()
